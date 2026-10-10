from .client import client

points = client.retrieve(
    collection_name="color_collection",
    ids=[1, 3],
    with_payload=True,
    with_vectors=True,
)

for point in points:
    print(f"ID: {point.id}")
    print(f"Payload: {point.payload}")
    print(f"Vector: {point.vector}")