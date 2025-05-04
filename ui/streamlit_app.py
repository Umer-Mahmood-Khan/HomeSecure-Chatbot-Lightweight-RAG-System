import streamlit as st
from retrieval import retrieve_context
from embeddings import load_embeddings
from prompt_builder import build_prompt
from mistral_runner import generate_answer
from agents.agent import HomeSecureAgent

st.set_page_config(
    page_title="HomeSecure Chatbot",
    page_icon="🏡",
)

st.title("🏡 HomeSecure Chatbot (RAG + Agent)")

# Initialize Agent
agent = HomeSecureAgent()

# Load embeddings once to avoid reloading on every query
@st.cache_resource
def get_embeddings():
    return load_embeddings()

docs, vectors = get_embeddings()

# Chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
query = st.text_input("Ask a question about home inspections:")

if st.button("Submit") and query:
    # Retrieve context
    top_chunks = retrieve_context(query, docs, vectors, k=2)
    context = "\n".join([f"{chunk}" for chunk, _ in top_chunks])

    # Agent handles the query first
    agent_response = agent.handle_query(query)

    if "address" in agent_response or "cost" in agent_response or "escalated" in agent_response:
        final_response = agent_response
        tool_used = True
    else:
        prompt = build_prompt(top_chunks, query)
        final_response = generate_answer(prompt)
        tool_used = False

    # Save to chat history
    st.session_state.chat_history.append(
        (query, final_response, context, tool_used)
    )

# Display chat history
if st.session_state.chat_history:
    st.subheader("Chat History")
    for idx, (q, response, ctx, tool) in enumerate(reversed(st.session_state.chat_history)):
        st.markdown(f"**User:** {q}")
        st.markdown(f"**Agent:** {response}")
        if tool:
            st.info("🛠 Tool Response")
        else:
            st.success("🤖 Mistral RAG Response")
        with st.expander("🔎 Retrieved Context"):
            st.markdown(ctx)
        st.markdown("---")
