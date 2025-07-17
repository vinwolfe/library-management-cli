import datetime

LENDING_FILE = "storage/lending.txt"

def load_lending():
    try:
        with open(LENDING_FILE, "r") as file:
            return [convert_to_lending_json(line) for line in file]
    except FileNotFoundError:
        open(LENDING_FILE, "w").close()
        return []

def add_lending(_book_id, _member_id):
    with open(LENDING_FILE, "a") as file:
        lending_date = datetime.date.today()
        file.write(f"{_book_id},{_member_id},{lending_date},nil\n")

def update_lending_return(_book_id):
    lending = load_lending()
    updated = []
    for record in lending:
        is_book_id = record["book_id"] == _book_id
        is_not_returned = record["return"] == "nil"

        if is_book_id and is_not_returned:
            return_date = datetime.date.today()
            updated.append(convert_to_lending_str({**record, "return": return_date}))
        else:
            updated.append(convert_to_lending_str(record))

    with open(LENDING_FILE, "w") as file:
        for line in updated:
            file.write(line)

def convert_to_lending_json(raw_data: str):
    data = raw_data.strip().split(",")
    return {
        "book_id": data[0],
        "member_id": data[1],
        "lent": data[2],
        "return": data[3],
    }

def convert_to_lending_str(json_data):
    return f"{json_data['book_id']},{json_data['member_id']},{json_data['lent']},{json_data['return']}\n"