from qdrant_client import QdrantClient, models
from .connect_cloud import client

client.create_collection(
    collection_name="products",
    vectors_config={
        "dense": models.VectorParams(size=384, distance=models.Distance.COSINE),
    },
    sparse_vectors_config={
        "sparse": models.SparseVectorParams(
            modifier=models.Modifier.IDF,
        ),
    },
)

client.create_payload_index(
    collection_name="products",
    field_name="in_stock",
    field_schema=models.PayloadSchemaType.BOOL,
)
client.create_payload_index(
    collection_name="products",
    field_name="sizes",
    field_schema=models.PayloadSchemaType.INTEGER,
)
client.create_payload_index(
    collection_name="products",
    field_name="price",
    field_schema=models.PayloadSchemaType.FLOAT,
)