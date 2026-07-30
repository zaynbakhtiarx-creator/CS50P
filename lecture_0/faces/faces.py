def main():
    Input = input('Input: ')
    print(convert(Input))


def convert(Input):
    return Input.replace(':)', '🙂').replace(':(', '😕')
    
main()