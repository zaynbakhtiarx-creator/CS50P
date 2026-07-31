def main():
    greeting = input('Greeting: ').strip().lower()
    print(fine(greeting))

def fine(g):
    if g.startswith('hello'):
        return '$0'
    elif g.startswith('h'):
        return '$20'
    else:
       return '$100'
main()