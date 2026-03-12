import requests

FINNHUB_KEY = "d6jvie1r01qkvh5riv20d6jvie1r01qkvh5riv2g"


def fetch(symbol):

    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_KEY}"

    try:

        r = requests.get(url, timeout=3)
        data = r.json()

        return {
            "price": round(data["c"],2),
            "change": round(data["dp"],2)
        }

    except:
        return {
            "price":"unavailable",
            "change":"unavailable"
        }


def get_sp500():
    return fetch("SPY")


def get_nasdaq():
    return fetch("QQQ")


def get_nikkei():
    return fetch("EWJ")


def get_hangseng():
    return fetch("EWH")


def get_dxy():
    return fetch("UUP")


def get_us10y():
    return fetch("TLT")


def get_crude_oil():
    return fetch("USO")