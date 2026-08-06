import sys
import requests


def main():
    try:
        bitcoin = float(sys.argv[1])
    except IndexError:
        sys.exit("Provide a Command-line Argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=355fe84ac302ae5478b4d313776acdc9be1b9bf8dca6b88ba037184250d976c3"
        )
    except requests.RequestException:
        sys.exit("Network error")

    data = response.json()
    price = float(data["data"]["priceUsd"])
    bitcoin_price = bitcoin * price
    print(f"${bitcoin_price:,.4f}")


if __name__ == "__main__":
    main()
