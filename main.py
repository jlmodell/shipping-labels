from datetime import datetime, timedelta
from blabel import LabelWriter
import csv
from rich import print


def main():
    label_writer = LabelWriter("labels.html", default_stylesheets=("style.css",))

    records = {}

    headers = [
        "num_of_labels",
        "po",
        "so",
        "name",
        "addr",
        "addr2",
        "city",
        "state",
        "zip_code",
    ]

    with open("queries.txt", "r") as queries:
        data = queries.readlines()

    _q = {x.split(" ")[0]: int(x.split(" ")[1]) for x in data}

    r = []

    for record in records.values():
        iterations, label_details = record

        print(iterations, type(iterations))

        for i in range(int(iterations)):
            temp = label_details.copy()
            temp["box"] = f"{i + 1} of {iterations}"
            r.append(temp)

    print(r)

    label_writer.write_labels(r, target="qrcode_and_label.pdf")


def query():
    today = (datetime.now() - timedelta(days=100)).strftime("%m-%d-%Y")
    q = """LISTB SA WITH F1 >= "{0}" F2 F3 F96 F97 F98 F99 F100""".format(today)

    print(q)


if __name__ == "__main__":
    import sys

    if sys.argv and sys.argv[1] == "query":
        query()
    else:
        main()
