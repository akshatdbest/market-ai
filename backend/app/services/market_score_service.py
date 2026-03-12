def calculate_market_score(data):

    score = 50   # neutral starting point

    # ----------------
    # GLOBAL MARKETS
    # ----------------

    if data["global"]["sp500"]["change"] != "unavailable":
        if data["global"]["sp500"]["change"] > 0:
            score += 5
        else:
            score -= 5

    if data["global"]["nasdaq"]["change"] != "unavailable":
        if data["global"]["nasdaq"]["change"] > 0:
            score += 5
        else:
            score -= 5

    if data["global"]["nikkei"]["change"] != "unavailable":
        if data["global"]["nikkei"]["change"] > 0:
            score += 3
        else:
            score -= 3

    if data["global"]["hangseng"]["change"] != "unavailable":
        if data["global"]["hangseng"]["change"] > 0:
            score += 3
        else:
            score -= 3


    # ----------------
    # INDIA MARKETS
    # ----------------

    if data["india"]["nifty"]["change"] != "unavailable":
        if data["india"]["nifty"]["change"] > 0:
            score += 10
        else:
            score -= 10

    if data["india"]["banknifty"]["change"] != "unavailable":
        if data["india"]["banknifty"]["change"] > 0:
            score += 7
        else:
            score -= 7


    # ----------------
    # AI NEWS SENTIMENT
    # ----------------

    if data["prediction"] == "Bullish":
        score += 10

    if data["prediction"] == "Bearish":
        score -= 10


    # ----------------
    # FINAL INTERPRETATION
    # ----------------

    if score >= 65:
        sentiment = "Strong Bullish"
    elif score >= 55:
        sentiment = "Bullish"
    elif score >= 45:
        sentiment = "Neutral"
    elif score >= 35:
        sentiment = "Bearish"
    else:
        sentiment = "Strong Bearish"


    return {
        "market_score": score,
        "sentiment": sentiment
    }