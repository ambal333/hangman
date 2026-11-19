from pathlib import Path


def read_file():
    words = []
    try:
        path = Path("./words/russian_words.txt")
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                words.append(line.strip())
    except FileNotFoundError:
        raise
    return words
