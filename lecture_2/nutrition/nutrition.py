def main():
    fruit_calories = {'Apple': 130,
            'Avocado': 50,
            'Banana': 110,
            'Cantaloupe': 50,
            'Grapefruit': 60, 
            'Grapes': 90,
            'Honeydew Melon': 50,
            'Kiwifruit': 90}
    get_calorie(fruit_calories)

def get_calorie(fruit_calories):
    item = input('Fruit: ').title()
    if item in fruit_calories:
        print(f'Caloreies: {fruit_calories[item]}')


main()