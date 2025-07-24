from . import model as m

import utils.helpers as h
from utils.constants import MAX_ATTEMPTS

from tabulate import tabulate

def handle_members_exist():
    members = m.load_members()
    if not members:
        return False
    return True

def handle_get_member(_member_id: str):
    return m.get_member(_member_id)

def handle_add_member():
    counter = 0
    signing_up = True

    while signing_up:
        while counter < MAX_ATTEMPTS:
            # Get user input for member id
            member_id = input("\nEnter member id: ")
            
            # If member ID already exists, increment counter and prompt again
            if m.compare_new_member(member_id):
                print("Member ID already registered")
                counter += 1
                continue

            # If member ID is unique, get name and contact information and save the member
            else:
                name = input("Enter name: ")
                contact = input("Enter contact: ")

                if m.save_member_to_file(member_id, name, contact):
                    print(f"Member added successfully")
                    signing_up = False
                    break
        else:
            if not h.handle_max_attempts():
                break
            counter = 0

        to_continue = h.handle_continue()
        if to_continue:
            counter = 0
            signing_up = True

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