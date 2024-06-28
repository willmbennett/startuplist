from fastapi import APIRouter
from api.models.startup import StartupCollection
import motor.motor_asyncio
import os
from dotenv import load_dotenv
load_dotenv(".env.local")  # Load variables from .env.local

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URI"])
db = client.prod
startup_collection = db.get_collection("startups")

router = APIRouter()

@router.get(
    "/api/startups",
    response_description="List all startups",
    response_model=StartupCollection,
    response_model_by_alias=False,
)
async def get_startups():
    return StartupCollection(startups=await startup_collection.find().to_list(2))