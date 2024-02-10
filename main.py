from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

raj_money_machine=MoneyMachine()

raj_coffee_maker=CoffeeMaker()

is_on=True

raj_menu=Menu()

while is_on:
    choice = input(f"What would you like? ({raj_menu.get_items()}): ")
    if choice == "report":
        raj_coffee_maker.report()
        raj_money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        drink = raj_menu.find_drink(choice)
        if raj_coffee_maker.is_resource_sufficient(drink):
            print(f"The total cost of the {drink.name} is: {drink.cost}")
            if raj_money_machine.make_payment(drink.cost):
                raj_coffee_maker.make_coffee(drink)

