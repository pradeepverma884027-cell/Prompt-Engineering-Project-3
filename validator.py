"""
validator.py

Responsible for validating AI responses.
"""


INVALID_RESPONSES = [
    "i don't know",
    "i do not know",
    "not sure",
    "unknown",
    "none",
    "n/a",
    "no information available",
    "information unavailable"
]


def validate_answer(answer):
    """
    Validate the response returned by Gemini.
    """
    if answer == "SERVICE_UNAVAILABLE":
        return (
            "⚠️ Gemini service is temporarily unavailable. "
            "Please try again later."
        )
    # Check if answer is None
    if answer is None:
        return "Information Not Found"

    # Remove extra spaces
    cleaned = answer.strip()

    # Check if answer is empty
    if cleaned == "":
        return "Information Not Found"

    # Convert to lowercase for comparison
    lower = cleaned.lower()

    # Check for invalid responses
    for invalid in INVALID_RESPONSES:
        if lower == invalid or lower.startswith(invalid):
            return "Information Not Found"

    # Return cleaned answer
    return cleaned