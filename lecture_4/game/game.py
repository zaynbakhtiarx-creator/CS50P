import random

def main():
    while True:
        try:
            n = int(input('n: '))
            if n > 0:
                break
        except ValueError: 
            print('Put the right format')

    random_int = random.randrange(1, n + 1)
    while True:
            try:

                 guess = int(input('Guess: '))
            except ValueError:
                print('Not a valid Input')
                continue
            if guess > 0:
                if guess < random_int:
                    print('Too small!')
                    
                elif guess > random_int: 
                    print('Too large!')
                    
                else:
                    print('Just right!')
                    break
            
main()
