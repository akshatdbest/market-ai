import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_gift_nifty():

    url = "https://query1.finance.yahoo.com/v8/finance/chart/NIFTY1!"

    try:

        r = requests.get(url, headers=HEADERS)

        data = r.json()

        result = data.get("chart", {}).get("result")

        if not result:
            return {"price": "unavailable", "change": "unavailable"}

        meta = result[0]["meta"]

        price = meta["regularMarketPrice"]
        prev = meta["previousClose"]

        change = ((price - prev) / prev) * 100

        return {
            "price": round(price,2),
            "change": round(change,2)
        }

    except Exception as e:

        print("gift nifty error:", e)

        return {
            "price": "unavailable",
            "change": "unavailable"
        }