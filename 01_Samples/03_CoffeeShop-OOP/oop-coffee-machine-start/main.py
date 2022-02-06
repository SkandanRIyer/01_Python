from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_is_on = True

while machine_is_on:
    choice_of_drink = input(f"What would you like? {menu.get_items()}:").lower()
    if choice_of_drink == "off":
        machine_is_on = False
        print("Byee...Byee...🙋‍🙋‍🙋‍🙋‍")
    elif choice_of_drink == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        orderItem = menu.find_drink(choice_of_drink)
        if type(orderItem) == MenuItem:
            if orderItem is not None:
                print(f"You have selected {choice_of_drink}.")
                if coffee_maker.is_resource_sufficient(orderItem):
                    if money_machine.make_payment(orderItem.cost):
                        coffee_maker.make_coffee(orderItem)
