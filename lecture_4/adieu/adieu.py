import inflect

def main():
    names = []
    p = inflect.engine()
    while True:
        try:

            name = input('Name: ')
            names.append(name)
            
        except EOFError:
            break
    print('Adieu, adieu, to', p.join(names))
if __name__ == '__main__':
    main()
    
      