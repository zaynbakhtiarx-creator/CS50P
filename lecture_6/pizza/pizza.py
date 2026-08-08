import sys
from tabulate import tabulate
import csv


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("File is not a csv")

    table(sys.argv[1])


def table(csv_file):
    try:
        with open(csv_file) as file:
            doc = csv.DictReader(file)
            print(tabulate(doc, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("file not found")


if __name__ == "__main__":
    main()
