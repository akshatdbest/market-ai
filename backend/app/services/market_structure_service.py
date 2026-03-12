import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


# -------------------------
# OPTION CHAIN PCR
# -------------------------

def get_option_pcr():

    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com/option-chain"
    }

    try:

        session = requests.Session()

        # first request generates cookies
        session.get("https://www.nseindia.com", headers=headers)

        r = session.get(url, headers=headers)

        data = r.json()

        total_put = data["filtered"]["PE"]["totOI"]
        total_call = data["filtered"]["CE"]["totOI"]

        pcr = round(total_put / total_call, 2)

        return {"pcr": pcr}

    except Exception as e:

        print("PCR error:", e)

        return {"pcr": "unavailable"}
# -------------------------
# MARKET BREADTH
# -------------------------

def get_market_breadth():

    url = "https://www.nseindia.com/api/allIndices"

    try:

        session = requests.Session()
        session.get("https://www.nseindia.com", headers=HEADERS)

        r = session.get(url, headers=HEADERS)

        data = r.json()

        for index in data["data"]:

            if index["index"] == "NIFTY 50":

                return {
                    "advances": index["advances"],
                    "declines": index["declines"],
                    "unchanged": index["unchanged"]
                }

    except Exception as e:

        print("Breadth error:", e)

    return {
        "advances": "unavailable",
        "declines": "unavailable",
        "unchanged": "unavailable"
    }