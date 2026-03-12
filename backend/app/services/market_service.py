import requests
from app.config import FINNHUB_API_KEY

BASE_URL = "https://finnhub.io/api/v1"

def get_sp500():

    url = f"{BASE_URL}/quote?symbol=SPY&token={FINNHUB_API_KEY}"

    response = requests.get(url)

    return response.json()