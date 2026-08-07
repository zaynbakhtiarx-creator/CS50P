import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    count_lines(sys.argv[1])


def count_lines(filename):
    try:
        with open(filename) as file:
            count = 0
            for line in file:
                if line.strip() == "":
                    continue
                if line.lstrip().startswith("#"):
                    continue

                count += 1

            print(count)

    except FileNotFoundError:
        sys.exit("File not exist")


main()
