from pathlib import Path
def read_file():
    words = []
    try:
        path = Path("./words/russian_words")
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                words.append(line.strip())
    except FileNotFoundError:
        return f"файла не существует"
    return words