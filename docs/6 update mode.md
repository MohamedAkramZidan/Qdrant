Qdrant normalizes vectors when using cosine similarity.

# update mode parameter:

    # upsert (default): Insert a point if it does not exist, or update it if it does.

    # insert_only: Insert a point only if it does not already exist. If a point with the same ID exists, the whole operation is ignored.

    # update_only: Update a point only if it already exists. Points that do not exist are not inserted.

`insert_only` mode is especially useful when migrating from one embedding model to another, where conflicts between regular updates and background re-embedding tasks need to be resolved.

![Embedding model migration in blue-green deployment](https://qdrant.tech/docs/embedding-model-migration.png)

Embedding model migration in blue-green deployment

`update_only` mode is useful with conditional updates. Because upserts default to inserts for non-existing points, a conditional update without an explicit `update_mode` will insert a new point even if the condition is not met, which is not the intended behavior in most cases.

### Named Vectors

If the collection was created with multiple vectors, each vector data can be provided using the vector’s name:

```python
client.upsert(
    collection_name="{collection_name}",
    points=[
        models.PointStruct(
            id=1,
            vector={
                "image": [0.9, 0.1, 0.1, 0.2],
                "text": [0.4, 0.7, 0.1, 0.8, 0.1, 0.1, 0.9, 0.2],
            },
        ),
        models.PointStruct(
            id=2,
            vector={
                "image": [0.2, 0.1, 0.3, 0.9],
                "text": [0.5, 0.2, 0.7, 0.4, 0.7, 0.2, 0.3, 0.9],
            },
        ),
    ],
)
```

Named vectors are optional. When uploading points, some vectors may be omitted. For example, you can upload one point with only the `image` vector and a second one with only the `text` vector.


