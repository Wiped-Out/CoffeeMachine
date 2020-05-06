#!/usr/bin/env python
class CoffeeMachine:
    has = {'Water': 400, 'Milk': 540, 'Beans': 120, 'Cups': 1, 'Money': 550}

    coffee_recipes = {
        1: {'Name': 'Espresso', 'Price': 4,
            'Resources': {'Water': 250, 'Milk': 0, 'Beans': 16, 'Cups': 1}},
        2: {'Name': 'Latte', 'Price': 7,
            'Resources': {'Water': 350, 'Milk': 75, 'Beans': 20, 'Cups': 1}},
        3: {'Name': 'Capuccino', 'Price': 6,
            'Resources': {'Water': 200, 'Milk': 100, 'Beans': 12, 'Cups': 1}}
    }

    def __init__(self):
        self.states = 'Choosing an action'

    def state(self, inp):
        if self.states == 'Choosing an action':
            if inp == 'buy':
                self.states = 'Choosing a type of coffee'
            elif inp == 'fill':
                self.states = 'Refilling'
                self.fill()
            elif inp == 'take':
                self.states = 'Taking money'
                self.take()
                self.states = 'Choosing an action'
            elif inp == 'remaining':
                self.states = 'Inventory check'
                self.remaining()
                self.states = 'Choosing an action'
            elif inp == 'exit':
                print('Bye!')
                exit()
        elif self.states == 'Choosing a type of coffee':
            self.buy(inp)

    def buy(self, usr_choice):
        if usr_choice == 'back':
            self.states = 'Choosing an action'
            return
        try:
            usr_choice = int(usr_choice)
            for key, value in self.coffee_recipes[usr_choice]['Resources'].items():
                if value > self.has[key]:
                    self.states = 'Choosing an action'
                    print(f'Sorry, not enough {key.lower()}')
                    return
            else:
                for key, value in self.coffee_recipes[usr_choice]['Resources'].items():
                    self.has[key] -= value
                self.has['Money'] += self.coffee_recipes[usr_choice]['Price']
                print('I have enough resources, making you a coffee!')
        except (ValueError, KeyError):
            print('Invalid option')
            self.states = 'Choosing a type of coffee'
            return

    def fill(self):
        try:
            print('Write how many ml of water do you want to add:')
            self.has['Water'] += int(input('> '))
            print('Write how many ml of milk do you want to add:')
            self.has['Milk'] += int(input('> '))
            print('Write how many grams of coffee  beans you want to add:')
            self.has['Beans'] += int(input('> '))
            print('Write how many disposable cups of coffee do you want to add:')
            self.has['Cups'] += int(input('> '))
            self.states = 'Choosing an action'
        except ValueError:
            self.states = 'Choosing an action'
            print('Error. Only integers are allowed')
            return

    def take(self):
        old_value = self.has['Money']
        self.has['Money'] -= self.has['Money']
        print(f'I gave you ${old_value}')

    def remaining(self):
        print('The coffee machine has:')
        for key, value in self.has.items():
            if key != 'Money':
                print(f'{value} of {key.lower()}')
            else:
                print(f'${value} of {key.lower()}')


machine = CoffeeMachine()

while True:
    if machine.states == "Choosing an action":
        machine.state(input("Write action (buy, fill, take, remaining, exit: "))
    elif machine.states == "Choosing a type of coffee":
        machine.state(input('What do you want to buy? 1 - Espresso, 2 - Latte, 3 - Cappucino - back - to menu'))
