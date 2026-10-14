from qdrant_client import models
from .connect_cloud import client
from .ingest_prod_data import DENSE_MODEL, SPARSE_MODEL

def hybrid_search(query_text, limit=4):
    return client.query_points(
        collection_name="products",
        # One sub-query per vector, both running in the same request
        prefetch=[
            models.Prefetch(
                query=models.Document(text=query_text, model=DENSE_MODEL),
                using="dense",
                # A prefetch limit must be at least the outer limit
                limit=20,
            ),
            models.Prefetch(
                query=models.Document(text=query_text, model=SPARSE_MODEL),
                using="sparse",
                limit=20,
            ),
        ],
        # Fusion merges the two candidate lists by rank position
        query=models.RrfQuery(rrf=models.Rrf()),
        limit=limit,
    ).points

for r in hybrid_search("Nike Pegasus 40"):
    print(f"{r.score:.4f}  {r.payload['title']}")