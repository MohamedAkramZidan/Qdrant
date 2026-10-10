from qdrant_client import models

from .client import client

# update_mode parameter:
    # upsert (default): Insert a point if it does not exist, or update it if it does.
    # insert_only: Insert a point only if it does not already exist. If a point with the same ID exists, the whole operation is ignored.
    # update_only: Update a point only if it already exists. Points that do not exist are not inserted.

client.upsert(
    collection_name="color_collection",
    points=[
        models.PointStruct(
            id=2,
            vector=[0.1, 0.9, 0.1],
            payload={
                "color": "green",
            },
        ),
        models.PointStruct(
            id=3,
            vector=[0.1, 0.1, 0.9],
            payload={
                "color": "blue",
            },
        ),
    ],
    update_mode=models.UpdateMode.INSERT_ONLY
)

client.upsert(
    collection_name="color_collection",
    points=[
        models.PointStruct(
            id=1,
            vector=[0.9, 0.1, 0.099],
            payload={
                "color": "red",
            },
        ),
    ],
    update_mode=models.UpdateMode.UPDATE_ONLY
)

# Qdrant normalizes vectors when using cosine similarity.