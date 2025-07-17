from . import model as m
from tabulate import tabulate

def handle_get_member(_member_id: str):
    return m.get_member(_member_id)

def handle_add_member():
    while True:
        member_id = input("Enter member id: ")
        if m.get_member(member_id):
            print("Member ID already exists")
        else:
            name = input("Enter name: ")
            contact = input("Enter contact: ")

            m.add_member(member_id, name, contact)
            print("Member added successfully")
            break

def handle_list_members():
    members = m.load_members()
    if len(members) == 0:
        print("No members found")
    else:
        rows = []
        for member in members:
            row = []
            for key in member.keys():
                row.append(member[key])
            rows.append(row)

        headers = [key.upper() for key in members[0].keys()]
        print(tabulate(rows, headers, tablefmt="rounded_grid"))