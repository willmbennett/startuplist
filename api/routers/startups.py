import logging
from fastapi import APIRouter, Query, Request, Body, HTTPException, status
from bson import ObjectId
from pymongo import ReturnDocument
from api.models.startup import StartupCollection, StartupModel, UpdateStartupModel
from api.utils.openai import get_vector_embeddings_from_openai

router = APIRouter(prefix='/api/startups')

@router.get(
    "",
    response_description="List all startups",
    response_model=StartupCollection,
    response_model_by_alias=False,
)
async def get_startups(request: Request, query: str = Query(..., description="The text string to be embedded")):
    logger = logging.getLogger(__name__)
    
    try:
        embeddings = get_vector_embeddings_from_openai(query)
    except Exception as e:
        logger.error("Error getting embeddings: %s", e)
        raise HTTPException(status_code=500, detail="Error getting embeddings")

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

    try:
        startups = await request.app.startup_collection.aggregate(agg).to_list(30)
    except Exception as e:
        logger.error("Error retrieving startups: %s", e)
        raise HTTPException(status_code=500, detail="Error retrieving startups")
    
    return StartupCollection(startups=startups)

@router.get(
    "/findexisting",
    response_description="Find an existing startup by scraped_url",
    response_model=bool,
    response_model_by_alias=False,
)
async def check_startup(request: Request, scraped_url: str = Query(..., description="url to check")):
    """
    Check to see if a startup already exists by the scraped_url.

    This route returns true or false.
    """
    print("About to check if this url exists")
    print(scraped_url)
    try:
        found_startup = await request.app.startup_collection.find_one({"scraped_url": scraped_url})
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
async def create_startup(request: Request, startup: StartupModel = Body(...)):
    """
    Insert a new startup record.

    A unique `id` will be created and provided in the response.
    """
    print('About to save startup')
    print(startup)
    try:
        new_startup = await request.app.startup_collection.insert_one(
            startup.model_dump(by_alias=True, exclude=["id"])
        )
        created_startup = await request.app.startup_collection.find_one(
            {"_id": new_startup.inserted_id}
        )
        return created_startup
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put(
    "/{id}",
    response_description="Update a startup",
    response_model=StartupModel,
    response_model_by_alias=False,
)
async def update_startup(request: Request, id: str, startup: UpdateStartupModel = Body(...)):
    """
    Update individual fields of an existing startup record.

    Only the provided fields will be updated.
    Any missing or `null` fields will be ignored.
    """
    startup = {
        k: v for k, v in startup.model_dump(by_alias=True).items() if v is not None
    }

    if len(startup) >= 1:
        try:
            update_result = await request.app.startup_collection.find_one_and_update(
                {"_id": ObjectId(id)},
                {"$set": startup},
                return_document=ReturnDocument.AFTER,
            )
            if update_result is not None:
                return update_result
            else:
                raise HTTPException(status_code=404, detail=f"Startup {id} not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # The update is empty, but we should still return the matching document:
    try:
        if (existing_startup := await request.app.startup_collection.find_one({"_id": ObjectId(id)})) is not None:
            return existing_startup
        else:
            raise HTTPException(status_code=404, detail=f"Startup {id} not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
