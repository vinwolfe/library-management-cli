import utils.helpers as h
import book.controller as books_controller
import member.controller as members_controller
import lending.controller as lending_controller
import services.lending_service as lending_service


h.print_greeting()
h.print_instructions()

commands_list = {
    "1": books_controller.handle_add_book,
    "2": members_controller.handle_add_member,
    "3": lending_service.handle_lending,
    "4": lending_service.handle_returning,
    "5": books_controller.handle_list_books,
    "6": members_controller.handle_list_members,
    "7": lending_controller.handle_list_lending,
}

running = True

def main():
    while running:
        command = input("Enter command: ")

        # This command will exit the application
        if command == "x":
            h.print_exit_message()
            break

        elif command in commands_list:
            commands_list[command]()
            print()

        # This command will handle displaying the instructions of the application
        elif command == "help":
            h.print_instructions()

        # This will ensure that no other commands are excepted
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()