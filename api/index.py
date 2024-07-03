import os
from fastapi import FastAPI
import logging
import uvicorn
from api.routers import startups
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(os.environ["MONGODB_URI"])
    app.mongodb = app.mongodb_client.prod
    app.startup_collection = app.mongodb.get_collection("startups")

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

logging.basicConfig(level=logging.INFO)
#app.include_router(yc_scraping2.router)
app.include_router(startups.router)

# Run FastAPI in debug mode
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
