def main():
    amount_due = 50
    while amount_due > 0:
        inserted_amount = int(input(f'Amount Due: {amount_due} \nInsert Coin: '))
        if inserted_amount in (25, 10, 5):
             amount_due -= inserted_amount
    print(f'Change Owed : {-(amount_due)}')
    
main()    