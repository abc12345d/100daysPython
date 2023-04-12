from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    # Prompt user by asking his/her choice
    user_choice = input(" What would you like? (espresso/latte/cappuccino/): ")

    if user_choice == "off":
        # turn off the machine
        is_on = False
    elif user_choice == "report":
        # print report
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(user_choice)

        # Check resources sufficient?
        if coffee_maker.is_resource_sufficient(drink):

            # Check transaction successful?
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
