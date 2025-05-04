# prompt_builder.py

def build_prompt(context_chunks, user_question):
    context = "\n".join(context_chunks)

    prompt = f"""Context:
{context}

Question:
{user_question}

Answer:"""

    return prompt
