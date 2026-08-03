def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (s[0:2].isalpha()):
        return False
    
    if not (2 <= len(s) <= 6):
        return False
    
    found_digit = False
    for char in s:
        if char.isdigit():
            if not found_digit and int(char) == 0:
                return False
            found_digit = True
            
        elif found_digit and char.isalpha():
            return False
    for char in s:
        if not char.isalpha() and not char.isdigit():
            return False
    
    return True
main()