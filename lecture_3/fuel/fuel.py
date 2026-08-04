def main():
    while True:
        fraction = input("Input: ")
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x >= 0 and y > 0 and x <= y:
                break
        except (ValueError, ZeroDivisionError):
            print(f"{fraction} is not the expected input")
            pass

    percent = percentage(x, y)
    print(percent)


def percentage(x, y):

    result = x / y

    percent = round(result * 100)
    if percent <= 1:
        return "E"
    if percent >= 99:
        return "F"
    return f"{percent}%"


main()
