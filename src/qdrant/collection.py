from qdrant_client.models import Distance, VectorParams
from .client import client

client.create_collection(
    collection_name="test_collection",
    vectors_config=VectorParams(size=4, distance=Distance.DOT),
)

client.create_collection(
    collection_name="color_collection",
    vectors_config=VectorParams(size=3, distance=Distance.COSINE),
)