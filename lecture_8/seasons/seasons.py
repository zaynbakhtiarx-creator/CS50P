from datetime import date
import inflect
import sys


def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")

    today_date = date.today()

    minutes = calculate_minutes(birth_date, today_date)

    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")

    print(words.capitalize(), "minutes")


def calculate_minutes(birth_date, today_date):
    time_passed = today_date - birth_date
    minutes = round(time_passed.total_seconds() / 60)
    return minutes


if __name__ == "__main__":
    main()
