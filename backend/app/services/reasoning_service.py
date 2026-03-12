def generate_reasoning(global_data, macro_data, prediction):

    reasons = []

    if global_data["nasdaq"]["change"] < 0:
        reasons.append("Nasdaq is falling indicating weak tech sentiment")

    if global_data["nikkei"]["change"] < 0:
        reasons.append("Nikkei decline signals Asian market weakness")

    if macro_data["crude_oil"]["change"] > 0:
        reasons.append("Crude oil rising may increase inflation pressure")

    if macro_data["us10y_bond"]["change"] > 0:
        reasons.append("Rising US10Y yield suggests tighter financial conditions")

    if not reasons:
        reasons.append("Markets showing mixed signals")

    return reasons