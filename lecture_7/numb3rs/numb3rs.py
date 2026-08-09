import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)

    if not match:
        return False

    numbers = match.groups()

    for number in numbers:
        if len(number) > 1 and number[0] == "0":
            return False

        if not 0 <= int(number) <= 255:
            return False

    return True


if __name__ == "__main__":
    main()
