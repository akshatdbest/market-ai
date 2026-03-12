def historical_market_reaction(news):

    # Basic keyword detection
    event_type = "general"

    joined_news = " ".join(news).lower()

    if "oil" in joined_news or "crude" in joined_news:
        event_type = "oil_spike"

    elif "war" in joined_news or "conflict" in joined_news:
        event_type = "geopolitical"

    elif "bank" in joined_news or "liquidity" in joined_news:
        event_type = "banking_crisis"

    elif "inflation" in joined_news or "rate hike" in joined_news:
        event_type = "interest_rate"


    historical_events = {

        "oil_spike": {
            "event": "Oil Spike (June 2022)",
            "nifty_move": "-1.8%",
            "banknifty_move": "-2.3%",
            "recovery_days": 3
        },

        "geopolitical": {
            "event": "Russia Ukraine War (Feb 2022)",
            "nifty_move": "-3.4%",
            "banknifty_move": "-4.1%",
            "recovery_days": 5
        },

        "banking_crisis": {
            "event": "Global Banking Crisis (Mar 2023)",
            "nifty_move": "-2.1%",
            "banknifty_move": "-3.0%",
            "recovery_days": 4
        },

        "interest_rate": {
            "event": "Fed Rate Hike Cycle (2022)",
            "nifty_move": "-1.2%",
            "banknifty_move": "-1.9%",
            "recovery_days": 2
        },

        "general": {
            "event": "Mixed Market Events",
            "nifty_move": "-0.5%",
            "banknifty_move": "-0.7%",
            "recovery_days": 1
        }
    }

    return historical_events[event_type]