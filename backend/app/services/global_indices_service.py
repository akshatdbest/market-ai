import requests

API_KEY = "d6jvie1r01qkvh5riv20d6jvie1r01qkvh5riv2g"

def fetch(symbol):

    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}"

    try:

        r = requests.get(url, timeout=10)

        data = r.json()

        if "c" in data and data["c"] != 0:

            return {
                "price": data["c"],
                "change": data["dp"]
            }

    except Exception as e:
        print("error:", e)

    return {"price":"unavailable","change":"unavailable"}


def get_sp500():
    return fetch("SPY")

def get_nasdaq():
    return fetch("QQQ")

def get_nikkei():
    return fetch("EWJ")

def get_hangseng():
    return fetch("EWH")