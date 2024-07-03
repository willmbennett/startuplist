import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from api.routers import startups
from api.utils.db import get_database, get_database_client

logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def db_lifespan(app: FastAPI):
    # Startup
    app.state.mongodb_client = get_database_client()
    app.state.mongodb = get_database(app.state.mongodb_client)
    ping_response = await app.state.mongodb.command("ping")
    if int(ping_response["ok"]) != 1:
        raise Exception("Problem connecting to database cluster.")
    else:
        logging.info("Connected to database cluster.")
    
    yield

    # Shutdown
    app.state.mongodb_client.close()

app = FastAPI(lifespan=db_lifespan)

app.include_router(startups.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
