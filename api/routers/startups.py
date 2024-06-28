import os
from fastapi import APIRouter, Query
from api.models.startup import StartupCollection
import motor.motor_asyncio

from api.utils.openai import get_vector_embeddings_from_openai

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
async def get_startups(query: str = Query(..., description="The text string to be embedded")):
    
    embeddings = get_vector_embeddings_from_openai(query)

    vectorSearchStage = {
        "$vectorSearch": {
            "index": "startups_vector_index",
            "path": "startups_embedding",
            "queryVector": embeddings,
            "numCandidates": 100,
            "limit": 30
        }
    }

    # Construct the aggregation pipeline with the dynamic vectorSearch stage
    agg = [
        vectorSearchStage,
    ]

    startups = await startup_collection.aggregate(agg).to_list(30)
    
    return StartupCollection(startups=startups)