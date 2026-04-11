from __future__ import annotations

import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv

from api_proxy import get_everything

MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"
DEFAULT_MISTRAL_MODEL = "mistral-small-latest"
APP_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT_FILE = APP_DIR / "text"


class MistralAPIError(Exception):
    """Ошибка при работе с Mistral API."""


def fetch_articles_for_last_day(
    news_api_key: str,
    topic: str,
    *,
    language: str = "en",
    page_size: int = 20,
) -> list[dict[str, Any]]:
    """Получает статьи по теме за последние сутки через NewsAPI."""
    now_utc = datetime.now(timezone.utc)
    # Используем начало предыдущего дня по UTC, чтобы не терять статьи,
    # опубликованные чуть раньше текущей минуты ровно сутки назад.
    day_ago_utc = (now_utc - timedelta(days=1)).replace(
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
    )

    response = get_everything(
        news_api_key,
        q=topic,
        from_param=day_ago_utc.isoformat(timespec="seconds").replace("+00:00", "Z"),
        to=now_utc.isoformat(timespec="seconds").replace("+00:00", "Z"),
        language=language,
        sort_by="publishedAt",
        page_size=page_size,
    )
    return response.get("articles", [])


def generate_articles_annotation(
    mistral_api_key: str,
    topic: str,
    articles: list[dict[str, Any]],
    *,
    model: str = DEFAULT_MISTRAL_MODEL,
) -> str:
    """Передаёт статьи в Mistral и возвращает аннотацию на русском языке."""
    if not articles:
        return (
            f"За последние сутки по теме '{topic}' в NewsAPI не найдено статей, "
            "поэтому аналитическую аннотацию составить нельзя."
        )

    article_payload = [
        {
            "title": article.get("title"),
            "description": article.get("description"),
            "content": article.get("content"),
            "source": (article.get("source") or {}).get("name"),
            "author": article.get("author"),
            "publishedAt": article.get("publishedAt"),
            "url": article.get("url"),
        }
        for article in articles
    ]

    messages = [
        {
            "role": "system",
            "content": (
                "Ты новостной аналитик. На основе переданного массива статей подготовь "
                "связную аналитическую аннотацию на русском языке объёмом 250-300 слов. "
                "Сосредоточься на том, что произошло за последний день по заданной теме, "
                "выдели главные события, общий контекст, возможные причины и последствия. "
                "Не выдумывай факты и явно указывай, если данных недостаточно."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Тема: {topic}\n"
                "Подготовь единый аналитический текст на русском языке без списков.\n"
                "Вот статьи за последние сутки:\n"
                f"{json.dumps(article_payload, ensure_ascii=False, indent=2)}"
            ),
        },
    ]

    try:
        response = requests.post(
            MISTRAL_API_URL,
            headers={
                "Authorization": f"Bearer {mistral_api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": messages,
                "temperature": 0.3,
                "max_tokens": 700,
                "response_format": {"type": "text"},
            },
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as error:
        raise MistralAPIError(f"Ошибка при запросе к Mistral API: {error}") from error
    except ValueError as error:
        raise MistralAPIError(f"Ошибка при чтении ответа Mistral API: {error}") from error

    try:
        content = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as error:
        raise MistralAPIError("Mistral API вернул неожиданный формат ответа.") from error

    if isinstance(content, str):
        return content.strip()

    if isinstance(content, list):
        text_chunks = [
            chunk.get("text", "").strip()
            for chunk in content
            if isinstance(chunk, dict) and chunk.get("type") == "text"
        ]
        annotation = "\n".join(chunk for chunk in text_chunks if chunk)
        if annotation:
            return annotation

    raise MistralAPIError("Не удалось извлечь текст аннотации из ответа Mistral API.")


def save_annotation(annotation: str, output_path: str | Path = DEFAULT_OUTPUT_FILE) -> Path:
    """Сохраняет аннотацию в файл."""
    target_path = Path(output_path)
    if not target_path.is_absolute():
        target_path = APP_DIR / target_path
    target_path.write_text(annotation, encoding="utf-8")
    return target_path


def run_daily_topic_analysis(
    news_api_key: str,
    mistral_api_key: str,
    topic: str,
    *,
    language: str = "en",
    page_size: int = 20,
    model: str = DEFAULT_MISTRAL_MODEL,
    output_path: str | Path = DEFAULT_OUTPUT_FILE,
) -> tuple[str, list[dict[str, Any]], Path]:
    """Полный сценарий: получает статьи, делает аннотацию и сохраняет её в файл."""
    articles = fetch_articles_for_last_day(
        news_api_key,
        topic,
        language=language,
        page_size=page_size,
    )
    annotation = generate_articles_annotation(
        mistral_api_key,
        topic,
        articles,
        model=model,
    )
    saved_path = save_annotation(annotation, output_path)
    return annotation, articles, saved_path


def main() -> None:
    load_dotenv(APP_DIR / ".env")

    news_api_key = os.getenv("NEWS_API_KEY")
    mistral_api_key = os.getenv("MISTRAL_API_KEY")
    topic = os.getenv("NEWS_TOPIC", "bitcoin")
    language = os.getenv("NEWS_LANGUAGE", "en")
    page_size = int(os.getenv("NEWS_PAGE_SIZE", "20"))
    model = os.getenv("MISTRAL_MODEL", DEFAULT_MISTRAL_MODEL)
    output_path = os.getenv("OUTPUT_FILE", str(DEFAULT_OUTPUT_FILE))

    if not news_api_key:
        raise RuntimeError("Ошибка: NEWS_API_KEY не найден в .env файле.")
    if not mistral_api_key:
        raise RuntimeError("Ошибка: MISTRAL_API_KEY не найден в .env файле.")

    annotation, articles, saved_path = run_daily_topic_analysis(
        news_api_key,
        mistral_api_key,
        topic,
        language=language,
        page_size=page_size,
        model=model,
        output_path=output_path,
    )

    print(f"Тема: {topic}")
    print(f"Найдено статей за последние сутки: {len(articles)}")
    print(f"Аннотация сохранена в: {saved_path}")
    print()
    print(annotation)


if __name__ == "__main__":
    main()
