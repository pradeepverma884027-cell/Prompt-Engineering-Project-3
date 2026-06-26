"""
document_loader.py

Responsible for:
1. Loading the document
2. Splitting it into paragraphs (chunks)
3. Numbering each chunk for citations
"""

import os


DOCUMENT_PATH = "sample_document.txt"


def load_document(file_path=DOCUMENT_PATH):
    """
    Loads the complete document as a string.

    Returns:
        str: Entire document text.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Document '{file_path}' not found."
        )

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def load_chunks(file_path=DOCUMENT_PATH):
    """
    Splits the document into paragraphs.

    Returns:
        list[str]: List of paragraph chunks.
    """

    document = load_document(file_path)

    chunks = [
        chunk.strip()
        for chunk in document.split("\n\n")
        if chunk.strip()
    ]

    return chunks


def load_numbered_chunks(file_path=DOCUMENT_PATH):
    """
    Returns numbered chunks.

    Example:
    [
        {
            "id": 1,
            "text": "Employees receive 20 days leave."
        },
        {
            "id": 2,
            "text": "Office timing is 9 AM to 6 PM."
        }
    ]
    """

    chunks = load_chunks(file_path)

    numbered_chunks = []

    for index, chunk in enumerate(chunks, start=1):

        numbered_chunks.append(
            {
                "id": index,
                "text": chunk
            }
        )

    return numbered_chunks