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

router = APIRouter()


@router.get("/global-markets")
def global_markets():

    return {

        "sp500": get_sp500(),

        "nasdaq": get_nasdaq(),

        "nikkei": get_nikkei(),

        "hangseng": get_hangseng(),

        "dxy": get_dxy(),

        "us10y_bond": get_us10y(),

        "crude_oil": get_crude_oil()
    }