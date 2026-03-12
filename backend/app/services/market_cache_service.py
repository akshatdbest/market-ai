from app.services.global_markets_service import (
    get_sp500,
    get_nasdaq,
    get_nikkei,
    get_hangseng,
    get_dxy,
    get_us10y,
    get_crude_oil
)

from app.services.prediction_service import market_prediction
from app.services.news_service import get_market_news
from app.services.levels_service import calculate_levels


MARKET_CACHE = {
    "global": None,
    "macro": None,
    "prediction": None,
    "news": None,
    "levels": None
}


def update_market_snapshot():
    try:
        print("Updating market cache...")

        global_data = {
            "sp500": get_sp500(),
            "nasdaq": get_nasdaq(),
            "nikkei": get_nikkei(),
            "hangseng": get_hangseng()
        }

        macro_data = {
            "dxy": get_dxy(),
            "us10y_bond": get_us10y(),
            "crude_oil": get_crude_oil()
        }

        prediction = market_prediction()
        news = get_market_news()

        # levels calculation
        levels = calculate_levels()

        MARKET_CACHE["global"] = global_data
        MARKET_CACHE["macro"] = macro_data
        MARKET_CACHE["prediction"] = prediction
        MARKET_CACHE["news"] = news
        MARKET_CACHE["levels"] = levels

        print("Market cache updated successfully")

    except Exception as e:
        print("Cache update failed:", e)