BOOKS_FILE = "storage/books.txt"

def load_books():
    try:
        with open(BOOKS_FILE, "r") as file:
            return [convert_to_book_json(line) for line in file]
    except FileNotFoundError:
        open(BOOKS_FILE, "w").close()
        return []

def get_book(_book_id: str):
    books = load_books()
    for book in books:
        if book["id"] == _book_id:
            return book
    return None

def add_book(_book_id, _title, _author, _availability):
    with open(BOOKS_FILE, "a") as file:
        file.write(f"{_book_id},{_title},{_author},{_availability}\n")

def update_book_availability(_book_id: str, _availability: bool):
    books = load_books()
    updated = []
    for book in books:
        if book["id"] == _book_id:
            updated.append(convert_to_book_str({**book, "available": _availability }))
        else:
            updated.append(convert_to_book_str(book))

    with open(BOOKS_FILE, "w") as file:
        for line in updated:
            file.write(line)

def convert_to_book_json(raw_data: str):
    data = raw_data.strip().split(",")
    return {
        "id": data[0],
        "title": data[1],
        "author": data[2],
        "available": data[3] == "True",
    }

def convert_to_book_str(json_data):
    return f"{json_data['id']},{json_data['title']},{json_data['author']},{json_data['available']}\n"