import os
from bson import ObjectId
from fastapi import APIRouter, Body, HTTPException, Query, status
from pymongo import ReturnDocument
from api.models.startup import StartupCollection, StartupModel, UpdateStartupModel
import motor.motor_asyncio

from api.utils.openai import get_vector_embeddings_from_openai

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URI"])
db = client.prod
startup_collection = db.get_collection("startups")

router = APIRouter(prefix='/api/startups')

@router.get(
    "",
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
            "limit": 10
        }
    }

    # Construct the aggregation pipeline with the dynamic vectorSearch stage
    agg = [
        vectorSearchStage,
    ]

    startups = await startup_collection.aggregate(agg).to_list(30)
    
    return StartupCollection(startups=startups)

@router.get(
    "/findexisting",
    response_description="Find an existing startup by scraped_url",
    response_model=bool,
    response_model_by_alias=False,
)
async def check_startup(scraped_url: str = Query(..., description="url to check")):
    """
    Check to see if a startup already exists by the scraped_url.

    This route returns true or false.
    """
    print("About to check if this url exists")
    print(scraped_url)
    try:
        found_startup = await startup_collection.find_one({"scraped_url": scraped_url})
        return found_startup is not None
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post(
    "",
    response_description="Add new startup",
    response_model=StartupModel,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_startup(startup: StartupModel = Body(...)):
    """
    Insert a new startup record.

    A unique `id` will be created and provided in the response.
    """
    print('About to save startup')
    print(startup)
    new_startup = await startup_collection.insert_one(
        startup.model_dump(by_alias=True, exclude=["id"])
    )
    created_startup = await startup_collection.find_one(
        {"_id": new_startup.inserted_id}
    )
    return created_startup

@router.put(
    "/{id}",
    response_description="Update a startup",
    response_model=StartupModel,
    response_model_by_alias=False,
)
async def update_startup(id: str, startup: UpdateStartupModel = Body(...)):
    """
    Update individual fields of an existing startup record.

    Only the provided fields will be updated.
    Any missing or `null` fields will be ignored.
    """
    startup = {
        k: v for k, v in startup.model_dump(by_alias=True).items() if v is not None
    }

    if len(startup) >= 1:
        update_result = await startup_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": startup},
            return_document=ReturnDocument.AFTER,
        )
        if update_result is not None:
            return update_result
        else:
            raise HTTPException(status_code=404, detail=f"Startup {id} not found")

    # The update is empty, but we should still return the matching document:
    if (existing_startup := await startup_collection.find_one({"_id": id})) is not None:
        return existing_startup

    raise HTTPException(status_code=404, detail=f"Startup {id} not found")