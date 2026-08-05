import emoji

def main():
    user_input = input('Emoji: ')
    print(emoji.emojize(user_input, language='alias'))

main()