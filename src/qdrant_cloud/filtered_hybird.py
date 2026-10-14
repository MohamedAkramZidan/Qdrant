from qdrant_client import models
from .connect_cloud import client
from .ingest_prod_data import DENSE_MODEL, SPARSE_MODEL

shopper_filter = models.Filter(
    must=[
        models.FieldCondition(key="in_stock", match=models.MatchValue(value=True)),
        models.FieldCondition(key="sizes",    match=models.MatchValue(value=11)),
    ]
)

def filtered_hybrid_search(query_text, query_filter, limit=4):
    return client.query_points(
        collection_name="products",
        prefetch=[
            models.Prefetch(
                query=models.Document(text=query_text, model=DENSE_MODEL),
                using="dense",
                # The filter goes here, not at the top level, so this
                # retriever spends its 20 candidates on eligible points
                filter=query_filter,
                limit=20,
            ),
            models.Prefetch(
                query=models.Document(text=query_text, model=SPARSE_MODEL),
                using="sparse",
                # The same filter, repeated for the second retriever
                filter=query_filter,
                limit=20,
            ),
        ],
        query=models.RrfQuery(rrf=models.Rrf()),
        limit=limit,
    ).points

for r in filtered_hybrid_search("Nike Pegasus 40", shopper_filter):
    print(f"{r.score:.4f}  {r.payload['title']}")