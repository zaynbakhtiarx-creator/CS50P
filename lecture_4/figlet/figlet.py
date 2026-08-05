import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    if len(sys.argv) == 1:
        figlet.setFont(font = random.choice(figlet.getfonts()))
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ['-f', '--font']:
            sys.exit('Invalid flag')
        if sys.argv[2] not in figlet.getFonts():
            sys.exit('Invalid font')
        figlet.setFont(font=sys.argv[2])
    else:
        sys.argv('Invalid arguments')
    text = input('String: ')
    print(figlet.renderText(text))


if __name__ == '__main__':
    main()