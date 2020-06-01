#!/usr/bin/env python
has = {'Water': 400, 'Milk': 540, 'Beans': 120, 'Cups': 9, 'Money': 550}

coffee_recipes = {
    1: {'Name': 'Espresso', 'Price': 4,
        'Resources': {'Water': 250, 'Milk': 0, 'Beans': 16, 'Cups': 1}},
    2: {'Name': 'Latte', 'Price': 7,
        'Resources': {'Water': 350, 'Milk': 75, 'Beans': 20, 'Cups': 1}},
    3: {'Name': 'Capuccino', 'Price': 6,
        'Resources': {'Water': 200, 'Milk': 100, 'Beans': 12, 'Cups': 1}}
}


def coffee_machine():
    global has
    print('What do you want to buy? 1 - Espresso, 2 - Latte, 3 - Cappucino, back - to main menu')
    usr_choice = input()
    if usr_choice == 'back':
        return
    usr_choice = int(usr_choice)
    for key, value in coffee_recipes[usr_choice]['Resources'].items():
        if value > has[key]:
            return f'Sorry, not enough {key.lower()}'
    else:
        for key, value in coffee_recipes[usr_choice]['Resources'].items():
            has[key] -= value
        has['Money'] += coffee_recipes[usr_choice]['Price']
        return 'I have enough resources, making you a coffee!'


def fill():
    global has
    print('Write how many ml of water do you want to add:')
    has['Water'] += int(input())
    print('Write how many ml of milk do you want to add:')
    has['Milk'] += int(input())
    print('Write how many grams of coffee  beans you want to add:')
    has['Beans'] += int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    has['Cups'] += int(input())
    return 'Done!'


def take():
    global has
    old_value = has['Money']
    has['Money'] -= has['Money']
    return f'I gave you ${old_value}'


def remaining():
    global has
    print('The coffee machine has:')
    for key, value in has.items():
        if key != 'Money':
            print(f'{value} of {key.lower()}')
        else:
            return f'${value} of {key.lower()}'


actions = {'Buy': coffee_machine, 'Fill': fill, 'Take': take, 'Remaining': remaining}

while True:
    print('Write action (buy, fill, take, remaining, exit):')
    action = input().capitalize()
    if action == 'exit'.capitalize():
        break
    else:
        print()
        print(actions[action]())
