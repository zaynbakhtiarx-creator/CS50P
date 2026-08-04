def main():
    items = {}
    grocery(items)
    for item in sorted(items):
         print(items[item], item.upper())

def grocery(items):
    while True:
        try: 
            item = input(' ').lower()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
            
        except EOFError:
            print()
            break
main()

