#!/usr/bin/env python
class CoffeeMachine:
    has = {
        'Water': 400,
        'Milk': 540,
        'Coffee beans': 120,
        'Disposable cups': 9,
        'Money': 550,
    }

    coffee_recipes = {
        1: {'Name': 'Espresso', 'Price': 4,
            'Resources': {'Water': 250, 'Milk': 0, 'Coffee beans': 16, 'Disposable cups': 1}},
        2: {'Name': 'Latte', 'Price': 7,
            'Resources': {'Water': 350, 'Milk': 75, 'Coffee beans': 20, 'Disposable cups': 1}},
        3: {'Name': 'Capuccino', 'Price': 6,
            'Resources': {'Water': 200, 'Milk': 100, 'Coffee beans': 12, 'Disposable cups': 1}},
    }

    def __init__(self):
        self.states = 'Choosing an action'
        self.refill = 'water'

    def state(self, inp):
        if self.states == 'Choosing an action':
            if inp == 'buy':
                self.states = 'Choosing a type of coffee'
            elif inp == 'fill':
                self.states = 'Refilling'
            elif inp == 'take':
                self.states = 'Taking money'
                self.take()
            elif inp == 'remaining':
                self.states = 'Inventory check'
                self.remaining()
            elif inp == 'exit':
                raise SystemExit('Bye!')
        elif self.states == 'Choosing a type of coffee':
            self.buy(inp)
        else:
            self.fill(inp)

    def buy(self, coffee):
        if coffee == 'back':
            self.states = 'Choosing an action'
            return
        try:
            coffee = int(coffee)
            for key, value in self.coffee_recipes[coffee]['Resources'].items():
                if value > self.has[key]:
                    self.states = 'Choosing an action'
                    print(f'Sorry, not enough {key.lower()}!\n')
                    return
                else:
                    self.has[key] -= value
            self.has['Money'] += self.coffee_recipes[coffee]['Price']
            self.states = 'Choosing an action'
            print('I have enough resources, making you a coffee!\n')
        except (ValueError, KeyError):
            print('Invalid option')
            self.states = 'Choosing a type of coffee'
            return

    def fill(self, amount: int):
        try:
            if self.refill == 'water':
                self.refill = 'milk'
                self.has['Water'] += int(amount)
            elif self.refill == 'milk':
                self.refill = 'beans'
                self.has['Milk'] += int(amount)
            elif self.refill == 'beans':
                self.refill = 'cups'
                self.has['Coffee beans'] += int(amount)
            elif self.refill == 'cups':
                self.refill = 'water'
                self.has['Disposable cups'] += int(amount)
                self.states = 'Choosing an action'
        except ValueError:
            self.states = 'Choosing an action'
            print('Error. Only integers are allowed')
            return

    def take(self):
        old_value = self.has['Money']
        self.has['Money'] -= self.has['Money']
        print(f'\nI gave you ${old_value}\n')
        self.states = 'Choosing an action'

    def remaining(self):
        print('\nThe coffee machine has:')
        for key, value in self.has.items():
            if key != 'Money':
                print(f'{value} of {key.lower()}')
            else:
                print(f'${value} of {key.lower()}\n')
                self.states = 'Choosing an action'


machine = CoffeeMachine()

while True:
    if machine.states == "Choosing an action":
        machine.state(input("Write action (buy, fill, take, remaining, exit):\n"))
    elif machine.states == "Choosing a type of coffee":
        print()
        machine.state(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n'))
    elif machine.states == 'Refilling':
        print('\nWrite how many ml of water do you want to add:')
        machine.state(int(input()))
        print('Write how many ml of milk do you want to add:')
        machine.state(int(input()))
        print('Write how many grams of coffee  beans you want to add:')
        machine.state(int(input()))
        print('Write how many disposable cups of coffee do you want to add:')
        machine.state(int(input()))
