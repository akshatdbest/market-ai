from app.services.global_markets_service import get_sp500, get_nasdaq


def market_prediction():

    sp = get_sp500()
    nq = get_nasdaq()

    score = 0

    if sp["change"] > 0:
        score += 1
    else:
        score -= 1

    if nq["change"] > 0:
        score += 1
    else:
        score -= 1

    if score > 0:
        direction = "Bullish"
    elif score < 0:
        direction = "Bearish"
    else:
        direction = "Sideways"

    probability = abs(score) * 50

    return {
        "direction": direction,
        "probability": probability
    }