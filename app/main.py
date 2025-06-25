from fastapi import FastAPI
import asyncio
from fastapi.concurrency import asynccontextmanager
from app.services.scheduler import start_scheduler
from app.routers import reservation, salle

@asynccontextmanager
async def startup_event(app: FastAPI):
    # Start the background scheduler
    await asyncio.create_task(start_scheduler())
    print("SCHEDULER: Scheduler started.")
    yield

app = FastAPI(
    title="A simple WMS",
    description="A simple WMS REST API built with FastAPI, SQLAlchemy, and SQLite",
    version="0.1.0",
    lifespan=startup_event
)

app.include_router(reservation.router)
app.include_router(salle.router)

@app.get("/")
async def root():
    return {"message": "Welcome to SimpleWMS!"}


