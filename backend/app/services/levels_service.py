def calculate_levels(global_data, prediction):

    try:

        sp = global_data["sp500"]["change"]
        nq = global_data["nasdaq"]["change"]

        bias = (sp + nq) / 2

        if prediction["direction"] == "Bullish":
            bias += 0.5
        elif prediction["direction"] == "Bearish":
            bias -= 0.5


        # Base reference levels
        nifty_price = 24000
        banknifty_price = 52000


        if bias > 0:
            nifty_support = nifty_price - 120
            nifty_resistance = nifty_price + 180
        else:
            nifty_support = nifty_price - 180
            nifty_resistance = nifty_price + 120


        if bias > 0:
            bank_support = banknifty_price - 300
            bank_resistance = banknifty_price + 450
        else:
            bank_support = banknifty_price - 450
            bank_resistance = banknifty_price + 300


        return {
            "nifty": {
                "support": round(nifty_support),
                "resistance": round(nifty_resistance)
            },
            "banknifty": {
                "support": round(bank_support),
                "resistance": round(bank_resistance)
            }
        }

    except Exception as e:

        print("Levels error:", e)

        return None