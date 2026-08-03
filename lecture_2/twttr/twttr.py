def main():
    word = input('Input: ')
    for word in word:
        if word not in ('a', 'e', 'i', 'o', 'u'):
            print(word, sep='', end='')

main()