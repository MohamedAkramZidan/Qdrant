Points can contain dense and sparse vectors.

A sparse vector is an array in which most of the elements have a value of zero.

It is possible to take advantage of this property to have an optimized representation, for this reason they have a different shape than dense vectors.

They are represented as a list of `(index, value)` pairs, where `index` is an integer and `value` is a floating point number. The `index` is the position of the non-zero value in the vector. The `values` are the values of the non-zero elements.

For example, the following vector:

```
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 0.0, 0.0]
```

can be represented as a sparse vector:

```
[(6, 1.0), (7, 2.0)]
```

Qdrant uses the following JSON representation throughout its APIs.

```json
{
  "indices": [6, 7],
  "values": [1.0, 2.0]
}
```

The `indices` and `values` arrays must have the same length. And the `indices` must be unique.

If the `indices` are not sorted, Qdrant will sort them internally so you may not rely on the order of the elements.

Sparse vectors must be named and can be uploaded in the same way as dense vectors.


```python
client.upsert(
    collection_name="{collection_name}",
    points=[
        models.PointStruct(
            id=1,
            vector={
                "text": models.SparseVector(
                    indices=[6, 7],
                    values=[1.0, 2.0],
                )
            },
        ),
        models.PointStruct(
            id=2,
            vector={
                "text": models.SparseVector(
                    indices=[1, 2, 3, 4, 5],
                    values=[0.1, 0.2, 0.3, 0.4, 0.5],
                )
            },
        ),
    ],
)
```