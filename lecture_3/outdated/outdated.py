def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                month, day, year = date.split("/")
                month, day, year = int(month), int(day), int(year)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(year, f'{month:02}', f'{day:02}', sep='-')
                    break
            elif "," in date:
                date = date.replace(",", "")
                month, day, year = date.split(" ")
                day, year = int(day), int(year)
                month = months.index(month) + 1
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(year, f'{month:02}', f'{day:02}', sep="-")
                    break
        except ValueError:
            continue


main()
