def count_vowels(text: str) -> int:
    vowels = "aeiouyąęó"
    return sum(1 for letter in text.lower() if letter in vowels)