# retrieval.py

import os
import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

# File paths
CHUNK_STORE_PATH = "embeddings_store/doc_chunks.pkl"
VECTOR_STORE_PATH = "embeddings_store/doc_vectors.pkl"
FAISS_INDEX_PATH = "faiss_index/index.faiss"

# Load the same embedding model used in embeddings.py
model = SentenceTransformer('all-MiniLM-L6-v2')

def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def embed_query(query):
    return model.encode([query])[0]  # Returns a single vector

def load_faiss_index():
    if not os.path.exists(FAISS_INDEX_PATH):
        raise FileNotFoundError("❌ FAISS index not found. Please run embeddings.py first.")
    return faiss.read_index(FAISS_INDEX_PATH)

def retrieve_context(query, chunks, vectors, k=2):
    query_vec = embed_query(query).astype("float32")

    # Build a temporary FAISS index in memory
    dim = vectors[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors).astype("float32"))

    # Search the index
    _, I = index.search(np.array([query_vec]), k)  # I = indices

    distances, indices = index.search(np.array([query_vec]), k)
    print("\n🔍 Top Matches:")
    for rank, (i, dist) in enumerate(zip(indices[0], distances[0])):
        print(f"[{rank+1}] Chunk #{i} (Distance: {dist:.4f})\n→ {chunks[i]}\n{'-'*40}")

    # Fetch top-k chunks
    results = [chunks[i] for i in I[0]]
    return results
