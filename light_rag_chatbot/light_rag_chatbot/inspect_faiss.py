# inspect_faiss.py

import faiss

FAISS_INDEX_PATH = "faiss_index/index.faiss"

index = faiss.read_index(FAISS_INDEX_PATH)

print("Is trained:", index.is_trained)
print("Total vectors in index:", index.ntotal)
