# 🏡 HomeSecure Chatbot – RAG + Rule-Based Agent System 🧠⚙️

This project is a fully local, offline chatbot system that combines **Retrieval-Augmented Generation (RAG)** with a **rule-based Agent architecture** for decision-making. It uses a static `.txt` knowledge base, vector search with FAISS, and a locally hosted **Mistral 7B** model for generation — no cloud, no APIs, no internet required.

---# HomeSecure Chatbot – RAG + Agent-Based Local System 🧠⚙️

This is the upgraded version of the HomeSecure chatbot — now enhanced with a **rule-based Agent layer** that brings decision-making and tool execution to a previously simple RAG pipeline. It runs fully **offline**, powered by a local Mistral 7B model and FAISS-based vector search over `.txt` documents.

---

## ✨ New Features

- 🔍 Context-aware retrieval via FAISS and `sentence-transformers`
- 🧠 Agent logic for intent detection and tool selection
- 🛠️ Built-in tools:
  - `book_inspection()`  
  - `show_pricing()`  
  - `escalate_to_human()`
- 🛡 Guardrails for topic relevance, missing info, and safe fallback
- 💬 Falls back to RAG + Mistral for general QnA
- 🖥️ Fully local CLI-based chatbot, future-ready for web UI
- 🔐 100% offline / air-gapped deployment

---

## 🧠 Tech Stack

| Component      | Tool/Library |
|----------------|--------------|
| Language Model | Mistral 7B via HuggingFace Transformers |
| Embeddings     | all-MiniLM-L6-v2 from `sentence-transformers` |
| Vector DB      | FAISS (in-memory flat index) |
| Agent Layer    | Custom Python class (rule-based logic) |
| Inference      | PyTorch + Accelerate |
| Language       | Python 3.10 |
| Interface      | Command-Line Interface (CLI) |

---

## 🔁 How It Works

1. Load and chunk `.txt` documents from `knowledge_base/`
2. Embed each chunk using `MiniLM-L6-v2`
3. Store vectors in a FAISS index
4. Accept user input from CLI
5. Agent analyzes intent:
   - If actionable → calls appropriate tool
   - Else → fallback to RAG prompt generation
6. Construct prompt:  
   **Context + User Question → Mistral → Answer**
7. Return final response to user

---

## 🧪 Sample Usage

```bash
$ python run_rag_cli.py

🏡 Welcome to HomeSecure QnA Chatbot (Light RAG + Agent)

You: I want to book an inspection

🤖 Agent: To book an inspection, please provide your address and preferred date.

You: 123 Main Street, May 5th

🤖 Agent: Booking confirmed for address: 123 Main Street, date: May 5th.

You: How much does an inspection cost?

🤖 Agent: Our standard home inspection costs $199.

You: Can you teach me to bake?

🛡️ Agent: I'm only able to assist with home inspection related queries.


## 📌 Project Phases Overview

```mermaid
graph LR
A[Phase 1: Light RAG Chatbot] --> B[Phase 2: RAG + Rule-Based Agent]
