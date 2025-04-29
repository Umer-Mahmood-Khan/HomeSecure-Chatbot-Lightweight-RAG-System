# inspect_vectors.py

import pickle
import numpy as np

VECTOR_STORE_PATH = "embeddings_store/doc_vectors.pkl"

with open(VECTOR_STORE_PATH, 'rb') as f:
    vectors = pickle.load(f)

vectors = np.array(vectors)

print("Vector store shape:", vectors.shape)  # (num_chunks, vector_dim)
