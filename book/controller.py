from . import model as b
from tabulate import tabulate

def handle_get_book(_book_id: str):
    return b.get_book(_book_id)

def handle_add_book():
    while True:
        book_id = input("Enter book id: ")
        if b.get_book(book_id):
            print("Book ID already exists")
        else:
            title = input("Enter title: ")
            author = input("Enter author: ")

            b.add_book(book_id, title, author, True)
            print("Book added successfully")
            break

def handle_mark_book_unavailable(_book_id: str):
    b.update_book_availability(_book_id, False)
    print("Book availability updated")

def handle_mark_book_available(_book_id: str):
    b.update_book_availability(_book_id, True)
    print("Book availability updated")

def handle_list_books():
    books = b.load_books()
    if len(books) == 0:
        print("No books found")
    else:
        rows = []
        for book in books:
            row = []
            for key in book.keys():
                row.append(book[key])
            rows.append(row)

            # print(book)

        headers = [key.upper() for key in books[0].keys()]
        print(tabulate(rows, headers, tablefmt="rounded_grid"))