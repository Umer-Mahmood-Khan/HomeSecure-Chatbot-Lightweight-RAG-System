# run_rag_cli.py

from embeddings import load_embeddings
from retrieval import retrieve_context
from prompt_builder import build_prompt
from mistral_runner import generate_answer
from agents.agent import HomeSecureAgent

def main():
    print("🏡 Welcome to HomeSecure QnA Chatbot (Light RAG + Agent)")

    agent = HomeSecureAgent()
    docs, vectors = load_embeddings()

    while True:
        query = input("\nYou: ")

        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        print("\n🔍 Retrieving context...")
        top_chunks = retrieve_context(query, docs, vectors, k=2)
        prompt = build_prompt(top_chunks, query)

        # 🔥 AGENT handles the query first
        agent_response = agent.handle_query(query)

        if "address" in agent_response or "cost" in agent_response or "escalated" in agent_response:
            # It means agent used a tool, no need to call Mistral
            print("\n🤖 Agent Response:")
            print(agent_response)
        else:
            # Else call Mistral model
            print("\n🤖 Generating answer...")
            answer = generate_answer(prompt)
            print("\n🤖 Mistral Response:")
            print(answer)

if __name__ == "__main__":
    main()
