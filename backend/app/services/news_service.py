import requests
from bs4 import BeautifulSoup

URL = "https://www.moneycontrol.com/news/business/markets/"

def get_market_news():

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []

    articles = soup.find_all("h2")

    for article in articles:

        text = article.get_text(strip=True)

        if text and len(text) > 20:
            headlines.append(text)

    return headlines[:15]