import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


# -------------------------
# INDIA VIX
# -------------------------

def get_india_vix():

    url = "https://www.nseindia.com/api/allIndices"

    try:

        session = requests.Session()
        session.get("https://www.nseindia.com", headers=HEADERS)

        r = session.get(url, headers=HEADERS)
        data = r.json()

        for index in data["data"]:

            if index["index"] == "INDIA VIX":

                return {
                    "value": index["last"],
                    "change": index["percentChange"]
                }

    except Exception as e:

        print("VIX error:", e)

    return {"value": "unavailable", "change": "unavailable"}


# -------------------------
# FII / DII FLOWS
# -------------------------

def get_fii_dii():

    url = "https://www.nseindia.com/api/fiidiiTradeReact"

    try:

        session = requests.Session()
        session.get("https://www.nseindia.com", headers=HEADERS)

        r = session.get(url, headers=HEADERS)

        data = r.json()

        # Sometimes response structure changes
        if isinstance(data, dict) and "data" in data:

            records = data["data"]

            fii = records[0]["netValue"]
            dii = records[1]["netValue"]

            return {
                "fii_net": fii,
                "dii_net": dii
            }

    except Exception as e:

        print("FII DII error:", e)

    return {
        "fii_net": "unavailable",
        "dii_net": "unavailable"
    }