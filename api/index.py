import os
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from api.routers import startups

logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def db_lifespan(app: FastAPI):
    # Startup
    app.mongodb_client = AsyncIOMotorClient(os.environ["MONGODB_URI"])
    app.mongodb = app.mongodb_client.prod
    ping_response = await app.mongodb.command("ping")
    print(app.mongodb)
    if int(ping_response["ok"]) != 1:
        raise Exception("Problem connecting to database cluster.")
    else:
        logging.info("Connected to database cluster.")
    
    yield

    # Shutdown
    app.mongodb_client.close()

app = FastAPI(lifespan=db_lifespan)

app.include_router(startups.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")