import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit(" Too few command line arguments")
    if len(sys.argv) > 3:
        sys.exit(" Too many command line arguments")
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, newline="") as before:
            reader = csv.DictReader(before)

            with open(output_file, "w", newline="") as after:
                writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(", ")
                    writer.writerow(
                        {"first": first, "last": last, "house": row["house"]}
                    )
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


if __name__ == "__main__":
    main()
