from qdrant_client import models
from .connect_cloud import client

# Name your collection
collection_name = "my_first_collection"

# Create it, describing the vectors it will hold
client.create_collection(
    collection_name=collection_name,
    vectors_config=models.VectorParams(
        size=4,  # each vector has 4 numbers
        distance=models.Distance.COSINE  # how we measure closeness
    )
)