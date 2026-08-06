import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):    
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        correct = False
        for j in range(3):
            try:
                user_answer = int(input(f'{x} + {y} = '))
            except ValueError:
                print('EEE')
                continue
            if user_answer == z:
                score += 1
                correct = True
                break
            else:
                print('EEE')
        if not correct:
            print(f'{x} + {y} = {z}')  
    print(f'Score: {score}')
    
def get_level():
    while True:
        try:
            level = int(input('Level: '))
        except ValueError:
            continue
        if level in [1, 2, 3]:
            return level

def generate_integer(level):
    if level == 1:
        return random.randrange(10)
    elif level == 2:
        return random.randrange(10, 100)
    elif level == 3:
        return random.randrange(100, 1000 )
    else:
        raise ValueError
   
                        
if __name__ == '__main__':
    main()