import requests
import time

session = requests.Session()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/option-chain"
}


def get_max_pain():

    try:

        # Step 1: get cookies
        session.get(
            "https://www.nseindia.com/option-chain",
            headers=HEADERS,
            timeout=5
        )

        time.sleep(1)

        # Step 2: fetch option chain
        url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

        r = session.get(url, headers=HEADERS, timeout=5)

        data = r.json()

        if "records" not in data:
            print("NSE option chain blocked")
            return {"max_pain": "unavailable"}

        option_data = data["records"]["data"]

        strike_losses = {}

        for row in option_data:

            strike = row.get("strikePrice")

            call_oi = row.get("CE", {}).get("openInterest", 0)
            put_oi = row.get("PE", {}).get("openInterest", 0)

            strike_losses[strike] = abs(call_oi - put_oi)

        max_pain = min(strike_losses, key=strike_losses.get)

        return {"max_pain": max_pain}

    except Exception as e:

        print("Max pain error:", e)

        return {"max_pain": "unavailable"}