def main():
    word = input("Input: ")
    shorten(word)
    print(word, sep="", end="")


def shorten(word):
    result = ""
    for word in word:
        if word.lower() not in "aeiou":
            result += word
    return result


if __name__ == "__main__":
    main()
