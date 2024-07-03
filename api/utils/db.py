import os
from motor.motor_asyncio import AsyncIOMotorClient

def get_database_client() -> AsyncIOMotorClient:
    return AsyncIOMotorClient(os.environ["MONGODB_URI"])

def get_database(client: AsyncIOMotorClient):
    return client.prod
