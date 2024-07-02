from fastapi import FastAPI
import logging
import uvicorn
from api.routers import yc_scraping2, startups

app = FastAPI()

logging.basicConfig(level=logging.INFO)
app.include_router(yc_scraping2.router)
app.include_router(startups.router)

# Run FastAPI in debug mode
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
