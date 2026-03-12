import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

def fetch_index(index):

    url = f"https://www.nseindia.com/api/equity-stockIndices?index={index}"

    try:

        session = requests.Session()
        session.get("https://www.nseindia.com", headers=HEADERS)

        r = session.get(url, headers=HEADERS)
        data = r.json()

        return {
            "price": data["data"][0]["lastPrice"],
            "change": data["data"][0]["pChange"]
        }

    except Exception:
        return {"price": "unavailable", "change": "unavailable"}


def fetch_market(symbol):

    try:

        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"

        r = requests.get(url, headers=HEADERS)

        data = r.json()

        meta = data["chart"]["result"][0]["meta"]

        price = meta["regularMarketPrice"]
        prev = meta["previousClose"]

        change = ((price - prev) / prev) * 100

        return {
            "price": round(price,2),
            "change": round(change,2)
        }

    except Exception:
        return {"price": "unavailable", "change": "unavailable"}


def get_nifty():
    return fetch_index("NIFTY 50")


def get_banknifty():
    return fetch_index("NIFTY BANK")


def get_sensex():
    return fetch_market("^BSESN")