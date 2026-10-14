from qdrant_client.models import Filter, FieldCondition, MatchValue
from .connect_cloud import client
from .ingest_data import model

query_text   = "automobile maintenance"
query_vector = list(model.embed([query_text]))[0].tolist()

results = client.query_points(
    collection_name="articles",
    query=query_vector,
    query_filter=Filter(
        must=[FieldCondition(key="category", match=MatchValue(value="automotive"))]
    ),
    limit=3,
)

for r in results.points:
    print(f"Score: {r.score:.3f}  |  {r.payload['title']}")