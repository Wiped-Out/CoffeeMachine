def can_i_make_coffee(water, milk, beans, cups):
    coffee = min((water // 200, milk // 50, beans // 15))
    difference = (coffee - cups)

    if cups <= coffee:
        if cups == 0 and coffee == 0:
            return "Yes, I can make that amount of coffee"
        else:
            return f"Yes, I can make that amount of coffee (and even {difference} more than that)"
    elif cups >= coffee:
        if cups == 1:
            return "No, I can make only 0 cup(s) of coffee"
        else:
            return f"No, I can make only {str(coffee)} cups of coffee"


print('Write how many ml of water the coffee machine has:')
water_ml = int(input())
print('Write how many ml of milk the coffee machine has:')
milk_ml = int(input())
print('Write how many grams of coffee beans the coffee machine has:')
beans_gr = int(input())
print('Write how many cups of coffee you will need:')
q_cups = int(input())
print(can_i_make_coffee(water_ml, milk_ml, beans_gr, q_cups))
