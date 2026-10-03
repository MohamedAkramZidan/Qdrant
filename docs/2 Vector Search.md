## The Representation Revolution

The latest research in Machine Learning for NLP is heavily focused on training Deep Language Models. In this process, the neural network takes a large corpus of text as input and creates a mathematical representation of the words in the form of vectors. These vectors are created in such a way that words with similar meanings and occurring in similar contexts are grouped together and represented by similar vectors. And we can also take, for example, an average of all the word vectors to create the vector for a whole text (such as query, sentence, or paragraph).

![deep neural](https://qdrant.tech/docs/gettingstarted/deep-neural.png)

We can take those **dense vectors** produced by the network and use them as a **different data representation**. They are dense because neural networks will rarely produce zeros at any position. In contrary to sparse ones, they have a relatively low dimensionality — hundreds or a few thousand only. Unfortunately, if we want to have a look and understand the content of the document by looking at the vector it’s no longer possible. Dimensions are no longer representing the presence of specific words.

Dense vectors can capture the meaning, not the words used in a text. That being said, **Large Language Models can automatically handle synonyms**. More so, since those neural networks might have been trained with multilingual corpora, they translate the same sentence, written in different languages, to similar vector representations, also called **embeddings**. And we can compare them to find similar pieces of text by calculating the distance to other vectors in our database.

![Input queries contain different words, but they are still converted into similar vector representations, because the neural encoder can capture the meaning of the sentences. That feature can capture synonyms but also different languages..](https://qdrant.tech/docs/gettingstarted/input.png)
**Vector search** is a process of finding similar objects based on their embeddings similarity. The good thing is, you don’t have to design and train your neural network on your own. Many pre-trained models are available, either on **HuggingFace** or by using libraries like [SentenceTransformers](https://www.sbert.net/?ref=hackernoon.com). If you, however, prefer not to get your hands dirty with neural models, you can also create the embeddings with SaaS tools

## Why Qdrant?

The challenge with vector search arises when we need to find similar documents in a big set of objects. If we want to find the closest examples, the naive approach would require calculating the distance to every document. That might work with dozens or even hundreds of examples but may become a bottleneck if we have more than that. When we work with relational data, we set up database indexes to speed things up and avoid full table scans. And the same is true for vector search. **Qdrant is a fully-fledged vector database** that speeds up the search process by using a graph-like structure to find the closest objects in sublinear time. So you don’t calculate the distance to every object from the database, but some candidates only.

