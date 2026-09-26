# Qdrant

A simple local setup for running [Qdrant](https://qdrant.tech/) with Docker and using it from Python.

## 1. Pull the Qdrant Image

```bash
docker pull qdrant/qdrant
```

## 2. Run Qdrant

Run the container with a fixed name and persistent storage:

```bash
docker run -d \
  --name qdrant \
  -p 6333:6333 \
  -p 6334:6334 \
  -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
  qdrant/qdrant
```

Qdrant will now be available at:

```text
http://localhost:6333
```

## 3. Install Dependencies

After cloning the repository, install the dependencies with:

```bash
uv sync

uv add qdrant-client
```

## 4. Project Structure

```text
src/
└── qdrant/
    ├── __init__.py
    ├── client.py
    ├── collection.py
    ├── insert.py
    └── search.py
```