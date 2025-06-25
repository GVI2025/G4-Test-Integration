from apscheduler.schedulers.background import BackgroundScheduler
from app.services.availability import update_room_availability
import asyncio

async def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_room_availability, 'interval', minutes=5)  # Adjust the interval as needed
    scheduler.start()

