from fastapi import APIRouter
from app.services.global_indices_service import *

router = APIRouter()

@router.get("/global-indices")
def global_indices():

    return {
        "sp500": get_sp500(),
        "nasdaq": get_nasdaq(),
        "nikkei": get_nikkei(),
        "hangseng": get_hangseng()
    }