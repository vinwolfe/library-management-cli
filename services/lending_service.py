import book.controller as book_controller
import member.controller as member_controller
import lending.controller as lending_controller

from utils.constants import MAX_ATTEMPTS
import utils.helpers as h

def handle_lending():
    book = None
    member = None
    lending = True

    # Check if there are available books to lend
    available_books = [b for b in book_controller.handle_books_exist() if b['is_available']]
    if len(available_books) == 0:
        print("No available books to lend.")
        return

    # Check if there are registered members 
    current_members = member_controller.handle_members_exist()
    if not current_members:
        print("No members registered.")
        return

    while lending and not book:
        book_counter = 0
        while book_counter < MAX_ATTEMPTS:
            # Get user input for book id
            book_id = input("\nEnter book id: ")

            # If book ID is valid, check availability and get member id
            temp_book = book_controller.handle_get_book(book_id)

             # Increment counter if book
            if temp_book is None:
                print("Book not found")
                book_counter += 1
                continue
            
            else:
                # Increment counter if book is not available
                if not temp_book['available']:
                    print("Book is not available")
                    book_counter += 1
                # Set book if found and available
                else:
                    book = temp_book
                    book_counter = 0
                    break
        else:
            # If max attempts reached, ask if user wants to continue
            if not h.handle_max_attempts():
                lending = False
                break
            book_counter = 0

    while lending and not member:
        member_counter = 0
        while member_counter < MAX_ATTEMPTS:
            # Get user input for member id
            member_id = input("Enter member id: ")

            # If member ID is valid, get member details
            temp_member = member_controller.handle_get_member(member_id)

            # Increment counter if member not found
            if temp_member is None:
                print("Member not found\n")
                member_counter += 1
                continue

            # Set member if found
            else:
                member = temp_member
                member_counter = 0
                break
        else:
            # If max attempts reached, ask if user wants to continue
            if not h.handle_max_attempts():
                lending = False
                break
            member_counter = 0

    # If user does not want to continue, exit the function
    if not lending:
        return

    print()
    book_controller.handle_mark_book_unavailable(book["id"])
    lending_controller.handle_add_lending(book["id"], member["id"])
    print("Book successfully lent")

def handle_returning():
    book = None
    returning = True

    # Check if there are lent books to return
    lent_books = [b for b in lending_controller.handle_get_lending() if b['return'] == 'nil']
    if len(lent_books) == 0:
        print("No books currently lent out.")
        return

    while returning and not book:
        book_counter = 0
        while book_counter < MAX_ATTEMPTS:
            # Get user input for book id
            book_id = input("\nEnter book id: ")

            # If book ID is valid, check availability and get member id
            temp_book = book_controller.handle_get_book(book_id)

            # Increment counter if book not
            if temp_book is None:
                print("Book not found")
                book_counter += 1
                continue
            else:
                # Increment counter if book is available (not lent)
                if temp_book['is_available']:
                    print("Book was not lent")
                    book_counter += 1
                # Set book if found and lent
                else:
                    book = temp_book
                    book_counter = 0
                    break
        else:
            # If max attempts reached, ask if user wants to continue
            if not h.handle_max_attempts():
                returning = False
                break
            book_counter = 0

    # If user does not want to continue, exit the function
    if not returning:
        return

    print()
    book_controller.handle_mark_book_available(book["id"])
    lending_controller.handle_update_lending_return(book["id"])
    print("Book successfully returned")