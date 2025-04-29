# HomeSecure Chatbot – Lightweight RAG System 🧠💬

This project is a lightweight, fully local Retrieval-Augmented Generation (RAG) chatbot designed for small-scale customer QnA use cases. It retrieves information from a static `.txt` knowledge base and generates natural language answers using a locally hosted Mistral 7B model — with **no cloud dependencies**.

---

## ✨ Features

- 🔍 Context-aware question answering using vector similarity search (FAISS)
- 🧠 Local inference with Mistral 7B (`transformers`, `torch`)
- 📦 Embedding with `SentenceTransformers` (`MiniLM-L6-v2`)
- 🖥️ CLI-based chatbot (web UI possible in future)
- 🔐 100% offline / air-gapped deployment

---

## 🧠 Tech Stack

| Component      | Tool/Library |
|----------------|--------------|
| Language Model | Mistral 7B via HuggingFace Transformers |
| Embeddings     | all-MiniLM-L6-v2 from `sentence-transformers` |
| Vector DB      | FAISS (in-memory flat index) |
| Inference      | PyTorch + GPU (float16) |
| Language       | Python |
| Interface      | Command-Line Interface (CLI) |

---

## 🔁 How It Works

1. Load and chunk `.txt` documents from `knowledge_base/`
2. Create embeddings for each chunk using MiniLM
3. Store those vectors in FAISS index
4. Accept user input from CLI
5. Embed the query and retrieve top-k similar chunks
6. Construct a custom prompt:  
   **Context + User Question → Mistral → Generated Answer**
7. Display final answer to user

---

## 🧪 Sample Usage

```bash
$ python run_rag_cli.py

Welcome to HomeSecure QnA Chatbot (Light RAG CLI)

You: Do you inspect homes in rural areas?

🔍 Retrieving context...
✅ Context found.

🤖 Generating answer...

Question: Do you inspect homes in rural areas?
Answer: Currently, countryside areas are under review and not actively served.
