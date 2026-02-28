# import requests as r
# import pprint
#
# result = r.get("GET https://newsapi.org/v2/everything?q=bitcoin&apiKey=c37e55c78e88403f88dc725fb613beae")
#
# pprint.pprint(result.json())


import os
from dotenv import load_dotenv
from api_proxy import get_top_headlines, get_everything, get_sources
from pprint import pprint

# Загружаем переменные окружения из .env
load_dotenv()

if __name__ == "__main__":
    # Читаем API ключ из переменной окружения
    API_KEY = os.getenv("NEWS_API_KEY")
    
    if not API_KEY:
        print("Ошибка: NEWS_API_KEY не найден в .env файле")
    else:
        print("--- Top Headlines ---")
        pprint(get_top_headlines(API_KEY, q="apple"))

        print("\n--- Everything ---")
        pprint(get_everything(API_KEY, q="bitcoin", page_size=1))

        print("\n--- Sources ---")
        pprint(get_sources(API_KEY, category="technology", language="en"))
