
# # def budget_animal_for_one_day():


# def zoo_budgeter():
#     animal_name = 'Zebras'
#     print('--- ZOO FOOD BUDGET ---')

#     # #### (start refactor here)
#     print('How many', animal_name, 'does our zoo have?')
#     animal_count = int(input('Count: '))
#     print('And how many pounds of food does each eat per day?')
#     food_count = int(input('Pounds: '))
#     food_quantity = animal_count * food_count
#     # #### (end refactor here)

#     print('And for how many days are we budgeting?')
#     day_count = int(input('Days: '))
#     total_pounds = day_count * food_quantity
#     print('Total pounds needed:', total_pounds)

# zoo_budgeter()



def budget_animal_for_one_day(animal_name):
    print('How many', animal_name, 'does our zoo have?')
    animal_count = int(input('Count: '))
    print('And how many pounds of food does each eat per day?')
    food_count = int(input('Pounds: '))
    food_quantity = animal_count * food_count
    return food_quantity

def zoo_budgeter():
    animal_name = 'Zebras'
    print('--- ZOO FOOD BUDGET ---')

    # #### (start refactor here)
    food_quantity = budget_animal_for_one_day(animal_name)
    # #### (end refactor here)

    print('And for how many days are we budgeting?')
    day_count = int(input('Days: '))
    total_pounds = day_count * food_quantity
    print('Total pounds needed:', total_pounds)

zoo_budgeter()