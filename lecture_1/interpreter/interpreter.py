def main():
    expression = input('Expression: ')
    x, y, z = expression.split(' ')
    answer = maths(x, y, z)
    print(f'{answer:.1f}')

def maths(x,y,z):
    x = float(x)
    z = float(z)
    if y == "+":
       return x + z
    elif y == "*":
      return  x * z   
    elif y == "-":
      return  x - z
    elif y == '/':  
      return  x / z    
    
main()