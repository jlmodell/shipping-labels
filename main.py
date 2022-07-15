from blabel import LabelWriter
import csv
from rich import print


def main():
    label_writer = LabelWriter(
        "labels.html", default_stylesheets=("style.css",))

    records = {}

    with open('addresses.txt', 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader, None)

        for row in reader:
            record = dict(zip(header, row))
            records[record['so']] = (record['num_of_labels'], record)

    r = []

    for record in records.values():
        iterations, label_details = record

        print(iterations, type(iterations))

        for i in range(int(iterations)):
            temp = label_details.copy()
            temp['box'] = f"{i + 1} of {iterations}"
            r.append(temp)

    print(r)

    label_writer.write_labels(r, target="qrcode_and_label.pdf")


if __name__ == "__main__":
    main()
