from fastapi import APIRouter
from app.services.index_service import get_nifty, get_banknifty, get_sensex

router = APIRouter()

@router.get("/indices")

def indices():

    return {
        "nifty": get_nifty(),
        "banknifty": get_banknifty(),
        "sensex": get_sensex()
    }