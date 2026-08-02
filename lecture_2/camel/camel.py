def main():
    camel_case = input('Word: ')
    snake_case(camel_case)

def snake_case(input):
    for letter in input:
        if letter.isupper():
            print('_', letter.lower(), sep='', end='')
        else:
            print(letter, end='')


main()
