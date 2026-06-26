"""
retriever.py

Responsible for finding the most relevant
document chunk for a user's question.
"""

STOP_WORDS = {
    "what", "is", "are", "the", "a", "an",
    "of", "to", "in", "on", "for", "with",
    "do", "does", "did", "how", "when",
    "where", "why", "who"
}

def preprocess(text):
    """
    Convert text into clean keywords.
    """

    words = text.lower().split()

    keywords = []

    for word in words:

        word = word.strip(".,?!()[]{}")

        if word and word not in STOP_WORDS:
            keywords.append(word)

    return keywords

def calculate_score(question_words, chunk):

    chunk_words = preprocess(chunk)

    score = 0

    for word in question_words:

        if word in chunk_words:
            score += 1

    return score

def retrieve_chunk(question, numbered_chunks):

    question_words = preprocess(question)

    best_chunk = None

    highest_score = -1

    for chunk in numbered_chunks:

        score = calculate_score(
            question_words,
            chunk["text"]
        )

        if score > highest_score:

            highest_score = score

            best_chunk = chunk

    return best_chunk