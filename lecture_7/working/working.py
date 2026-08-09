import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(
        r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s
    )

    if not match:
        raise ValueError

    hour1, minute1, period1, hour2, minute2, period2 = match.groups()

    hour1 = int(hour1)
    hour2 = int(hour2)

    minute1 = int(minute1) if minute1 else 0
    minute2 = int(minute2) if minute2 else 0

    if not (1 <= hour1 <= 12):
        raise ValueError

    if not (1 <= hour2 <= 12):
        raise ValueError

    if not (0 <= minute1 <= 59):
        raise ValueError

    if not (0 <= minute2 <= 59):
        raise ValueError

    if period1 == "AM":
        if hour1 == 12:
            hour1 = 0
    else:
        if hour1 != 12:
            hour1 += 12

    if period2 == "AM":
        if hour2 == 12:
            hour2 = 0
    else:
        if hour2 != 12:
            hour2 += 12

    return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"


if __name__ == "__main__":
    main()
