from fastapi import APIRouter
from app.services.prediction_service import market_prediction

router = APIRouter()

@router.get("/prediction")

def predict():

    return {"prediction":market_prediction()}