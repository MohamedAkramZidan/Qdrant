Vector databases are a relatively new way for interacting with abstract data representations derived from opaque machine learning models such as deep learning architectures. These representations are often called vectors or embeddings and they are a compressed version of the data used to train a machine learning model to accomplish a task like sentiment analysis, speech recognition, object detection, and many others.

These new databases shine in many applications like semantic search and recommendation systems

- **points** → Qdrant's basic stored objects. A point typically contains:
    - **Vector** → embedding representation.
    - **Payload** → metadata/additional information.
    - **ID** → identifies the point.
- **Payload** → can be used for:
    - Filtering searches.
    - Returning useful information alongside the matching vector.
    - Storing metadata such as `document_id`, `category`, `author`, etc.

![[Pasted image 20260918024947.png]]

A point in Qdrant consists of an ID, one or more vectors, and optionally a payload. Points are stored inside collections.

Collection same as table in SQL DB

### benefits of using vector databases include:
1. Efficient storage and indexing of high-dimensional data.
2. Ability to handle large-scale datasets with billions of data points.
3. Support for real-time analytics and queries.
4. Ability to handle vectors derived from complex data types such as images, videos, and natural language text.
5. Improved performance and reduced latency in machine learning and AI applications.
6. Reduced development and deployment time and cost compared to building a custom solution.

![[Pasted image 20260918025900.png]]
- [Collections](https://qdrant.tech/documentation/manage-data/collections/): A collection is a named set of points (vectors with a payload) among which you can search. The vector of each point within the same collection must have the same dimensionality and be compared by a single metric. [Named vectors](https://qdrant.tech/documentation/manage-data/collections/#collection-with-multiple-vectors) can be used to have multiple vectors in a single point, each of which can have their own dimensionality and metric requirements.
- [Distance Metrics](https://en.wikipedia.org/wiki/Metric_space): These are used to measure similarities among vectors and they must be selected at the same time you are creating a collection. The choice of metric depends on the way the vectors were obtained and, in particular, on the neural network that will be used to encode new queries.
- [Points](https://qdrant.tech/documentation/manage-data/points/): The points are the central entity that Qdrant operates with and they consist of a vector and an optional id and payload.
    - id: a unique identifier for your vectors.
    - Vector: a high-dimensional representation of data, for example, an image, a sound, a document, a video, etc.
    - [Payload](https://qdrant.tech/documentation/manage-data/payload/): A payload is a JSON object with additional data you can add to a vector.
- [Storage](https://qdrant.tech/documentation/manage-data/storage/): Qdrant persists data on disk, and [lets you choose](https://qdrant.tech/documentation/ops-configuration/memory-tiers/) how much of it also lives in memory: `pinned` to keep hot data fully in RAM, `cached` for a warm disk cache, or `cold` to save RAM on large datasets.
- [Clients](https://qdrant.tech/documentation/interfaces/): the programming languages you can use to connect to Qdrant.


- **Pinned** → keeps data **fully in RAM** for fast access.
- **Cached** → uses **RAM as a cache** while the main data remains on disk.
- **Cold** → keeps data mainly on **disk** to reduce RAM usage.