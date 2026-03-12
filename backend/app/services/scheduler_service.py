from apscheduler.schedulers.background import BackgroundScheduler
from app.services.market_cache_service import update_market_snapshot


def start_scheduler():

    scheduler = BackgroundScheduler()

    scheduler.add_job(
        update_market_snapshot,
        "interval",
        minutes=5
    )

    scheduler.start()

    print("Market scheduler started")