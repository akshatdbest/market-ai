def calculate_market_score(global_data, indices_data, sentiment):

    score = 0

    # GLOBAL MARKETS
    if global_data["sp500"]["change"] > 0:
        score += 1
    else:
        score -= 1

    if global_data["nasdaq"]["change"] > 0:
        score += 1
    else:
        score -= 1

    if global_data["nikkei"]["change"] > 0:
        score += 1
    else:
        score -= 1

    if global_data["hangseng"]["change"] > 0:
        score += 1
    else:
        score -= 1


    # INDIAN MARKETS TREND
    if indices_data["nifty"]["change"] > 0:
        score += 1
    else:
        score -= 1


    if indices_data["banknifty"]["change"] > 0:
        score += 1
    else:
        score -= 1


    # NEWS SENTIMENT
    if sentiment == "positive":
        score += 2
    elif sentiment == "negative":
        score -= 2


    return score



def get_market_prediction(score):

    if score >= 4:
        return "Strong Bullish"

    if score >= 2:
        return "Bullish"

    if score == 0:
        return "Neutral"

    if score <= -4:
        return "Strong Bearish"

    return "Bearish"