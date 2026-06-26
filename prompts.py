def build_prompt(context, question):

    return f"""
You are an AI assistant.

Answer ONLY using the Reference Document below.

Rules:

1. Never use outside knowledge.

2. Never guess.

3. If the answer is not present,
reply exactly:

Information Not Found

4. Keep the answer short and accurate.

5. Do not explain anything outside the document.

Reference Document:

{context}

Question:

{question}

Answer:
"""