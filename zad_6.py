import re


def word_frequencies(text: str) -> dict:
    words = re.findall(r"[^\W_]+", text.lower())
    result = {}

    for word in words:
        result[word] = result.get(word, 0) + 1

    return result