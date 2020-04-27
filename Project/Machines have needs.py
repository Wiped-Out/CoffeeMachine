# Write your code here
def coffee_machine(cups):
    print(f'For {cups} of coffee you will need:')
    water = f'{200 * cups} ml of water'
    milk = f'{50 * cups} ml of milk'
    beans = f'{15 * cups} g of coffee beans'
    return f'{water} \n{milk} \n{beans}'


print('Write how many cups of coffee you will need:')

usr_cups = int(input())

print(coffee_machine(usr_cups))
