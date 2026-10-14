from qdrant_client.models import PointStruct
from fastembed import TextEmbedding
from .connect_cloud import client

model = TextEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")  # 384-dim

documents = [
    {"id": 1, "text": "Car repair guide",  "category": "automotive"},
    {"id": 2, "text": "How to cook pasta",  "category": "food"},
]

points = [
    PointStruct(
        id=doc["id"],
        vector=vector.tolist(),
        payload={"title": doc["text"], "category": doc["category"]},
    )
    for doc, vector in zip(documents, model.embed([d["text"] for d in documents]))
]
# upload_points handles batching and retries automatically; preferred for lists of points.
# upsert is the raw operation, better for single points or small real-time updates.
client.upload_points(collection_name="articles", points=points)