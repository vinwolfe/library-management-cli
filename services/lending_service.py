# from ..book import controller as book_controller
# from ..member import controller as member_controller
# from ..lending import controller as lending_controller

import book.controller as book_controller
import member.controller as member_controller
import lending.controller as lending_controller

def handle_lending():
    book = None
    member = None

    while book is None:
        book_id = input("Enter book id: ")
        temp_book = book_controller.handle_get_book(book_id)
        if not temp_book is None:
            if temp_book["available"] is True:
                book = temp_book
            else:
                print("Book not available to lend")
        else:
            print("Book not found")

    while member is None:
        member_id = input("Enter member id: ")
        temp_member = member_controller.handle_get_member(member_id)
        if not temp_member is None:
            member = temp_member
        else:
            print("Member not found")

    book_controller.handle_mark_book_unavailable(book["id"])
    lending_controller.handle_add_lending(book["id"], member["id"])
    print("Book successfully lent")

def handle_returning():
    book = None

    while book is None:
        book_id = input("Enter book id: ")
        temp_book = book_controller.handle_get_book(book_id)
        if not temp_book is None:
            if temp_book["available"] is False:
                book = temp_book
            else:
                print("Book was not lent")
        else:
            print("Book not found")

    book_controller.handle_mark_book_available(book["id"])
    lending_controller.handle_update_lending_return(book["id"])
    print("Book successfully returned")