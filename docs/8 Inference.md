# Qdrant Inference

## What is Qdrant Inference?

Qdrant Inference means you can give Qdrant the **raw data** (such as text) instead of generating the vector yourself.

### Normal Approach

```text
Text
 ↓
Embedding Model
 ↓
Vector
 ↓
Qdrant
```

You are responsible for running the embedding model.

```python
vector = embedding_model.encode("hello world")

client.upsert(
    collection_name="docs",
    points=[
        models.PointStruct(
            id=1,
            vector=vector,
        )
    ],
)
```

---

## With Qdrant Inference

```text
Text
 ↓
Qdrant Inference
 ↓
Embedding Model
 ↓
Vector
 ↓
Qdrant
```

Example:

```python
client.upsert(
    collection_name="docs",
    points=[
        models.PointStruct(
            id=1,
            vector=models.Document(
                text="hello world",
                model="your-model",
            ),
        )
    ],
)
```

You provide:

- Text
    
- Model name
    

Qdrant handles the embedding generation.

---

## Important

Inference **does not mean there is no model**.

The model still has to run:

```text
Inference = running the model to convert data → vector
```

The difference is **who manages that inference**.

|Approach|Who runs/manages the embedding model?|
|---|---|
|Normal|You / your embedding service|
|Qdrant Inference|Qdrant's inference infrastructure|

---

## Production Architecture

Qdrant Inference can simplify the architecture:

```text
App
 ↓
Qdrant
 ↓
Embedding Model
```

But companies may also use a separate embedding service:

```text
App
 ↓
Embedding Service
 ↓
Embedding Model
 ↓
Qdrant
```

A separate embedding service gives more control over:

- Scaling
    
- Batching
    
- Model versions
    
- GPU/CPU resources
    
- Monitoring
    
- A/B testing
    
- Model migration
    
- Custom or fine-tuned models