from __future__ import annotations

from typing import Any, Optional, Dict
import requests

BASE_URL = "https://newsapi.org/v2"  # без "/" в конце


class NewsAPIError(Exception):
    """Ошибка при работе с NewsAPI."""


def _make_request(endpoint: str, api_key: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{BASE_URL}/{endpoint}"
    final_params: Dict[str, Any] = {"apiKey": api_key}

    if params:
        # добавляем только непустые параметры
        final_params.update({k: v for k, v in params.items() if v is not None})

    try:
        response = requests.get(url, params=final_params, timeout=10)
        # если хотите строго по HTTP:
        response.raise_for_status()

        data = response.json()

        # если хотите строго по протоколу NewsAPI:
        if isinstance(data, dict) and data.get("status") == "error":
            raise NewsAPIError(f"NewsAPI error: {data.get('code')} - {data.get('message')}")

        return data

    except requests.exceptions.RequestException as e:
        raise NewsAPIError(f"Ошибка при запросе к NewsAPI ({endpoint}): {e}") from e
    except ValueError as e:
        raise NewsAPIError(f"Ошибка при парсинге JSON ({endpoint}): {e}") from e


def get_top_headlines(
    api_key: str,
    q: str = None,
    country: str = None,
    category: str = None,
    sources: str = None,
    page_size: int = None,
    page: int = None,
) -> Dict[str, Any]:
    params = {
        "q": q,
        "country": country,
        "category": category,
        "sources": sources,
        "pageSize": page_size,
        "page": page,
    }
    return _make_request("top-headlines", api_key, params)


def get_everything(
    api_key: str,
    q: str = None,
    q_in_title: str = None,
    sources: str = None,
    domains: str = None,
    exclude_domains: str = None,
    from_param: str = None,
    to: str = None,
    language: str = None,
    sort_by: str = None,
    page_size: int = None,
    page: int = None,
) -> Dict[str, Any]:
    params = {
        "q": q,
        "qInTitle": q_in_title,
        "sources": sources,
        "domains": domains,
        "excludeDomains": exclude_domains,
        "from": from_param,
        "to": to,
        "language": language,
        "sortBy": sort_by,
        "pageSize": page_size,
        "page": page,
    }
    return _make_request("everything", api_key, params)


def get_sources(
    api_key: str,
    category: str = None,
    language: str = None,
    country: str = None,
) -> Dict[str, Any]:
    params = {"category": category, "language": language, "country": country}
    return _make_request("top-headlines/sources", api_key, params)