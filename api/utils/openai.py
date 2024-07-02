from fastapi import HTTPException
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(".env.local")  # Load variables from .env.local
openai_client = OpenAI()

def get_vector_embeddings_from_openai(query):
    try:
        # Fetch the embeddings for the input query
        response = openai_client.embeddings.create(
            input=query,
            model="text-embedding-3-small"
        )
        embeddings = response.data[0].embedding
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch embeddings")
    
    return embeddings
