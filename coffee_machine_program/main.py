#%%
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 3,
    "milk": 2,
    "coffee": 10,
    "money": 0
}


def get_report():
    report = f"Water: {resources['water']}ml\n"
    report += f"Milk: {resources['milk']}ml\n"
    report += f"Coffee: {resources['coffee']}g\n"
    report += f"Money: ${resources['money']:.1f}\n"

    return report


def check_resources(drink):
    '''get drink and return (True, []) 
    if there are enough resources to make that drink,
    otherwise (False, a list of depleted resources)'''
    depleted_ingredients = []
    for ingredient, quantity in MENU[drink]["ingredients"].items():
        if resources[ingredient] < quantity:
            depleted_ingredients.append(ingredient)

    return (True, []) if len(depleted_ingredients) == 0 else (False, depleted_ingredients)

is_off = False
while not is_off:
    user_input = input(" What would you like? (espresso/latte/cappuccino):")

    if user_input == "off":
        # Turn off the Coffee Machine
        is_off = True

    elif user_input == "report":
        # Print report
        print(get_report())

    else:
        drink = user_input

        # Check resources sufficient?
        is_ingredient_sufficient, depleted_ingredients = check_resources(drink)
        if not is_ingredient_sufficient:
            
            ingredient_insufficient_message = "Sorry there is not enough "
            if len(depleted_ingredients) > 1:
                ingredient_insufficient_message += f"{', '.join(depleted_ingredients[:-1])} and "
            ingredient_insufficient_message += f"{depleted_ingredients[-1]}. "
            
            print(ingredient_insufficient_message)

            # Not enough ingredients -> end current session
            continue

        else:
            # Process coins.
            print(f"Please insert coins.")

            quarter = float(input("How many quarters?: "))
            dime = float(input("How many dimes?: "))
            nickle = float(input("How many nickles?: "))
            penny = float(input("How many pennies?: "))

            coins_inserted = quarter * 0.25 + dime * 0.1 + nickle * 0.05 + penny * 0.01
            
            # Check transaction successful?
            if coins_inserted < MENU[drink]["cost"]:
                print("Sorry that's not enough money. Money refunded.")

                # Not enough money -> end current session    
                continue

            else:
                # offer change
                change = coins_inserted - MENU[drink]["cost"]
                if change > 0:
                    print(f"Here is ${change:.2f} dollars in change.")

                # Make Coffee
                # update resources 
                resources["money"] += MENU[drink]["cost"]
                for ingredient, quantity in MENU[drink]["ingredients"].items():
                    resources[ingredient] -= quantity
                
                print(f"Here is your {drink}. Enjoy!")
