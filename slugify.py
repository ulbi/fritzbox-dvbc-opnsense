"""Helper function to convert text to URL-friendly slug format."""

import re
import unicodedata


def slugify(text: str) -> str:
    """
    Convert text to URL-friendly slug format.

    Transliterates German umlauts and special characters, removes
    non-alphanumeric characters, and converts to lowercase with hyphens.

    Args:
        text: Input text to slugify.

    Returns:
        URL-friendly slug string.
    """
    if not text:
        return ""

    # Transliteration map for German umlauts and special characters
    transliterations = {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "ß": "ss",
        "Ä": "Ae",
        "Ö": "Oe",
        "Ü": "Ue",
    }

    # Apply transliterations
    for char, replacement in transliterations.items():
        text = text.replace(char, replacement)

    # Normalize unicode characters (e.g., accented characters)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")

    # Convert to lowercase
    text = text.lower()

    # Replace non-alphanumeric characters with hyphens
    text = re.sub(r"[^a-z0-9]+", "-", text)

    # Remove leading and trailing hyphens
    text = text.strip("-")

    return text