def generate_trade_setup(levels, prediction):

    setup = {}

    # NIFTY
    nifty_support = levels["nifty"]["support"]
    nifty_resistance = levels["nifty"]["resistance"]

    if prediction["direction"] == "Bullish":

        setup["nifty"] = {
            "action": "Buy Above",
            "entry": nifty_resistance,
            "target": nifty_resistance + 200,
            "stoploss": nifty_support
        }

    else:

        setup["nifty"] = {
            "action": "Sell Below",
            "entry": nifty_support,
            "target": nifty_support - 200,
            "stoploss": nifty_resistance
        }


    # BANKNIFTY
    bank_support = levels["banknifty"]["support"]
    bank_resistance = levels["banknifty"]["resistance"]

    if prediction["direction"] == "Bullish":

        setup["banknifty"] = {
            "action": "Buy Above",
            "entry": bank_resistance,
            "target": bank_resistance + 400,
            "stoploss": bank_support
        }

    else:

        setup["banknifty"] = {
            "action": "Sell Below",
            "entry": bank_support,
            "target": bank_support - 400,
            "stoploss": bank_resistance
        }

    return setup