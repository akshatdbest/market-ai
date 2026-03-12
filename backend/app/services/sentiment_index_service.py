import random

def get_fear_greed_index():

    score = random.randint(20,80)

    if score < 25:
        sentiment = "Extreme Fear"
    elif score < 45:
        sentiment = "Fear"
    elif score < 55:
        sentiment = "Neutral"
    elif score < 75:
        sentiment = "Greed"
    else:
        sentiment = "Extreme Greed"

    return {
        "score": score,
        "sentiment": sentiment
    }