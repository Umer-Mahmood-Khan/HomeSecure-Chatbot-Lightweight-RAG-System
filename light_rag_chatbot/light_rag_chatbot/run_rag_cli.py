# run_rag_cli.py

from embeddings import load_embeddings
from retrieval import retrieve_context
from prompt_builder import build_prompt
from mistral_runner import generate_answer

def main():
    print("Welcome to HomeSecure QnA Chatbot (Light RAG CLI)\n")
    query = input("You: ")

    print("\n🔍 Retrieving context...")
    docs, vectors = load_embeddings()
    top_chunks = retrieve_context(query, docs, vectors, k=2)

    print("✅ Context found.\n")

    prompt = build_prompt(top_chunks, query)

    print("🤖 Generating answer...\n")
    answer = generate_answer(prompt)

    print("\n----------------------")
    print(f"Question: {query}")
    print(f"Answer: {answer}")
    print("----------------------\n")

if __name__ == "__main__":
    main()
