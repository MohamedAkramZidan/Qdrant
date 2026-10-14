from qdrant_client import models
from .connect_cloud import client

client.create_collection(
    collection_name="articles",
    vectors_config=models.VectorParams(
        size=384,
        distance=models.Distance.COSINE,
    ))

# Qdrant Cloud runs in strict mode, which rejects filtered queries on payload
# fields that aren't indexed. Step 4 filters on "category", so create that
# index now, before ingesting or querying.
client.create_payload_index(
    collection_name="articles",
    field_name="category",
    field_schema=models.PayloadSchemaType.KEYWORD,
)