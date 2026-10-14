from qdrant_client import models
from .connect_cloud import client

CATALOG = [
    (1, "Nike Pegasus 40 running shoes",              139, True,  [8, 9, 10, 11]),
    (2, "Nike Pegasus 41 running shoes",              145, True,  [9, 10, 11]),
    (3, "Nike Pegasus Trail 4 trail running shoes",   149, True,  [9, 10]),
    (4, "Nike Invincible 3 road running shoes",       179, True,  [10, 11]),
    (5, "Adidas Ultraboost 22 running shoes",         189, False, [9, 10]),
    (6, "Brooks Ghost 15 neutral running shoes",      129, True,  [10, 11]),
    (7, "Nike Air Zoom Structure 25 stability shoes", 129, True,  [9, 10]),
    (8, "Nike Pegasus 40 womens running shoes",       139, False, [6, 7, 8]),
]

DENSE_MODEL  = "sentence-transformers/all-MiniLM-L6-v2"
SPARSE_MODEL = "Qdrant/bm25"

client.upsert(
    collection_name="products",
    points=[
        models.PointStruct(
            id=pid,
            vector={
                "dense":  models.Document(text=title, model=DENSE_MODEL),
                "sparse": models.Document(text=title, model=SPARSE_MODEL),
            },
            payload={"title": title, "price": price, "in_stock": stock, "sizes": sizes},
        )
        for pid, title, price, stock, sizes in CATALOG
    ],
)