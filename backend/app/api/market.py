from fastapi import APIRouter
from app.services.market_service import get_sp500

router = APIRouter()

@router.get("/market/sp500")
def sp500():

    return get_sp500()