MEMBERS_FILE = "storage/members.txt"

def load_members():
    try:
        with open(MEMBERS_FILE, "r") as file:
            return [convert_to_member_json(line) for line in file]
    except FileNotFoundError:
        open(MEMBERS_FILE, "w").close()
        return []

def get_member(member_id):
    members = load_members()
    for member in members:
        if member["id"] == member_id:
            return member
    return None

def add_member(_id: str, _name: str, _contact: str):
    with open(MEMBERS_FILE, "a") as file:
        file.write(f"{_id},{_name},{_contact}\n")


def convert_to_member_json(raw_data: str):
    data = raw_data.strip().split(",")
    return {
        "id": data[0],
        "name": data[1],
        "contact": data[2]
    }

def convert_to_member_str(json_data):
    return f"{json_data['id']},{json_data['name']},{json_data['contact']}\n"