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
    x    : Exit
    
    """)

def print_exit_message():
    print("Thank you for using the Library Management System. Goodbye!\n")