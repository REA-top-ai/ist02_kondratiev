import os
import sys
from dotenv import load_dotenv

# Добавляем корневой каталог проекта в sys.path, чтобы импортировать api_proxy из app_news
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app_news')))

from api_proxy import get_everything  # type: ignore

def analyze_news(api_key: str, query: str = "technology") -> list:
    """
    Получает новости и отбирает 50 статей по заданным критериям:
    - title не пустое и не состоит только из пробелов
    - url не None (проверяем наличие http/https)
    - description имеет длину не менее 50 символов.
    """
    filtered_news = []
    page = 1

    # Запрашиваем страницы, пока не наберём 50 новостей
    while len(filtered_news) < 50:
        response = get_everything(api_key, q=query, page_size=100, page=page)
        
        if "articles" not in response or not response["articles"]:
            # Если нет статей или ошибка, прерываем цикл
            break

        articles = response["articles"]

        for article in articles:
            title = article.get("title")
            url = article.get("url")
            description = article.get("description")

            # 1. Проверка title (не пустое и не содержит только пробел)
            if not title or not str(title).strip():
                continue
                
            # 2. Проверка url (не None и простой тест валидности)
            if not url or not (url.startswith("http://") or url.startswith("https://")):
                continue
                
            # 3. Проверка description (длина не менее 50 символов)
            if not description or len(str(description)) < 50:
                continue

            # Формируем итоговый словарь нужного формата
            source_name = article.get("source", {}).get("name") if isinstance(article.get("source"), dict) else None
            
            filtered_article = {
                "title": str(title).strip(),
                "source": source_name,
                "publishedat": article.get("publishedAt"),
                "Author": article.get("author")
            }
            
            filtered_news.append(filtered_article)
            
            # Если собрали 50 удовлетворяющих критериям, выходим из цикла
            if len(filtered_news) >= 50:
                break
                
        page += 1

    return filtered_news

if __name__ == "__main__":
    # Загружаем переменные окружения, предполагая наличие файла .env на уровень выше
    # либо в этой директории
    dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app_news', '.env'))
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        load_dotenv()
        
    API_KEY = os.getenv("NEWS_API_KEY")
    
    if not API_KEY:
        print("Ошибка: NEWS_API_KEY не найден в переменных окружения.")
    else:
        results = analyze_news(API_KEY, query="world")
        print(f"Отобрано новостей: {len(results)}")
        
        import json
        with open(os.path.join(os.path.dirname(__file__), 'results.json'), 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
            
        print("Результаты сохранены в results.json")
        if results:
            print("\nПример первой новости:")
            print(json.dumps(results[0], ensure_ascii=False, indent=4))
