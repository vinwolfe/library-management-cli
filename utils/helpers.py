import pyfiglet

def print_greeting():
    f = pyfiglet.figlet_format("Library Management System", font="ogre")
    print(f"\n{f}\n")

def print_instructions():
    print("""
    1    : Add a new book
    2    : Register a new member
    3    : Lend a book
    4    : Return a book
    5    : Display books inventory
    6    : Display members information
    7    : Display lending records
    
    help : Show Instructions
    exit : Exit
    
    """)

def print_exit_message():
    print("Thank you for using the Library Management System. Goodbye!\n")

def handle_max_attempts():
    print("\nYou have reached the maximum attempts.")
    to_continue = input("Would you like to continue? (yes/no): ").strip().lower()
    if to_continue == 'yes':
        return True
    elif to_continue == 'no':
        print("\nReturning to main menu\n")
        return False

def handle_continue(text: str = "Would you like to perform this action again? (yes/no): "):
    to_continue = input("\n" + text).strip().lower()
    if to_continue == 'yes':
        return True
    elif to_continue == 'no':
        print("Returning to main menu.")
        return False
    else:
        print("Invalid input. Returning to main menu.")
        return False
