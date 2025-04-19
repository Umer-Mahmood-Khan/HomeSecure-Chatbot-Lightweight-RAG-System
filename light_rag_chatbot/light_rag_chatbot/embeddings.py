# embeddings.py

import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

KB_PATH = "knowledge_base/faq.txt"
CHUNK_STORE_PATH = "embeddings_store/doc_chunks.pkl"
VECTOR_STORE_PATH = "embeddings_store/doc_vectors.pkl"
FAISS_INDEX_PATH = "faiss_index/index.faiss"

# Load a small, fast embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def read_chunks_from_file():
    with open(KB_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    chunks = [chunk.strip() for chunk in content.split("\n\n") if chunk.strip()]
    return chunks

def embed_chunks(chunks):
    return model.encode(chunks, show_progress_bar=True)

def save_pickle(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)

def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def build_faiss_index(vectors):
    dim = vectors[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    faiss.write_index(index, FAISS_INDEX_PATH)
    return index

def load_embeddings():
    if os.path.exists(CHUNK_STORE_PATH) and os.path.exists(VECTOR_STORE_PATH):
        print("📦 Loading precomputed embeddings...")
        chunks = load_pickle(CHUNK_STORE_PATH)
        vectors = load_pickle(VECTOR_STORE_PATH)
    else:
        print("🚀 Creating embeddings from scratch...")
        chunks = read_chunks_from_file()
        vectors = embed_chunks(chunks)
        os.makedirs("embeddings_store", exist_ok=True)
        save_pickle(chunks, CHUNK_STORE_PATH)
        save_pickle(vectors, VECTOR_STORE_PATH)
        print("✅ Embeddings saved.")
    
    #print(f"Loaded {len(chunks)} chunks with {len(vectors)} vectors.")
        # Debug print chunks
    print(f"\n🧩 Loaded {len(chunks)} knowledge base chunks:\n")
    for i, chunk in enumerate(chunks):
        print(f"[{i}] {chunk}\n{'-'*50}")


    build_faiss_index(vectors)
    return chunks, vectors
