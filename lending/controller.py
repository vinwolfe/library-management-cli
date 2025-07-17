from . import model as l
from tabulate import tabulate

def handle_add_lending(_book_id: str, _member_id: str):
    l.add_lending(_book_id, _member_id)
    print("Lending record saved")

def handle_update_lending_return(_book_id: str):
    l.update_lending_return(_book_id)
    print("Lending record updated")

def handle_list_lending():
    lending = l.load_lending()
    if len(lending) == 0:
        print("No lending records found")
    else:
        rows = []
        for record in lending:
            row = []
            for key in record.keys():
                row.append(record[key])
            rows.append(row)

        headers = [key.upper() for key in lending[0].keys()]
        print(tabulate(rows, headers, tablefmt="rounded_grid"))
