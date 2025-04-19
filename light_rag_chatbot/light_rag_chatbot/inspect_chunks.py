# inspect_chunks.py

import pickle

CHUNK_STORE_PATH = "embeddings_store/doc_chunks.pkl"

with open(CHUNK_STORE_PATH, 'rb') as f:
    chunks = pickle.load(f)

print(f"Total Chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks):
    print(f"[{i}] {chunk}\n{'-'*40}")
