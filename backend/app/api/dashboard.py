from fastapi import APIRouter

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
from app.services.reasoning_service import generate_reasoning
from app.services.trade_setup_service import generate_trade_setup
from app.services.historical_reaction_service import historical_market_reaction  # NEW IMPORT


router = APIRouter()


@router.get("/market-intelligence")
def market_intelligence():

    # GLOBAL MARKETS
    global_data = {
        "sp500": get_sp500(),
        "nasdaq": get_nasdaq(),
        "nikkei": get_nikkei(),
        "hangseng": get_hangseng()
    }

    # MACRO INDICATORS
    macro_data = {
        "dxy": get_dxy(),
        "us10y_bond": get_us10y(),
        "crude_oil": get_crude_oil()
    }

    # AI PREDICTION
    prediction = market_prediction()

    # MARKET NEWS
    news = get_market_news()

    # SUPPORT / RESISTANCE LEVELS
    levels = calculate_levels(global_data, prediction)

    # AI MARKET REASONING
    reasoning = generate_reasoning(global_data, macro_data, prediction)

    # AI TRADE SETUP
    trade_setup = generate_trade_setup(levels, prediction)

    # HISTORICAL MARKET REACTION  (NEW)
    historical = historical_market_reaction(news)

    return {
        "global": global_data,
        "macro": macro_data,
        "prediction": prediction,
        "news": news,
        "levels": levels,
        "reasoning": reasoning,
        "trade_setup": trade_setup,
        "historical_reaction": historical  # NEW FIELD
    }