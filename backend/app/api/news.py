from fastapi import APIRouter
from app.services.news_service import get_market_news
from app.services.sentiment_service import analyze_sentiment

router = APIRouter()

@router.get("/news")

def news():

    headlines = get_market_news()

    results = []

    for h in headlines:

        sentiment = analyze_sentiment(h)

        results.append({
            "headline": h,
            "sentiment": sentiment
        })

    return results