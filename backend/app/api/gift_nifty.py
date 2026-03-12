from fastapi import APIRouter
from app.services.gift_nifty_service import get_gift_nifty

router = APIRouter()

@router.get("/gift-nifty")
def gift():

    return {
        "gift_nifty": get_gift_nifty()
    }