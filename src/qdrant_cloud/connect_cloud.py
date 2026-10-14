from qdrant_client import QdrantClient
from qdrant_cloud.config import settings

def create_qdrant_client() -> QdrantClient:
    return QdrantClient(
        url=settings.qdrant_url,
        api_key=settings.qdrant_api_key.get_secret_value(),
        timeout=10,
    )

client = create_qdrant_client()
collections = client.get_collections()
print(f"Connected to Qdrant Cloud: {len(collections.collections)} collections")