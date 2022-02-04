from menu import MENU, resources

collection = 0.00


def water_needed(drink_prepared):
    """
    returns the water needed to prepare a drink
    :param drink_prepared: the name of the drink to be prepared
    :return: quantity in ml
    """
    return MENU[drink_prepared]["ingredients"]["water"]


def milk_needed(drink_prepared):
    """
    returns the milk needed to prepare a drink
    :param drink_prepared: the name of the drink to be prepared
    :return: quantity in ml
    """
    return MENU[drink_prepared]["ingredients"]["milk"]


def coffee_needed(drink_prepared):
    """
    returns the coffee needed to prepare a drink
    :param drink_prepared: the name of the drink to be prepared
    :return: quantity in ml
    """
    return MENU[drink_prepared]["ingredients"]["coffee"]


def water_remaining():
    """
    returns the water remaining in the machine
    """
    return resources["water"]


def milk_remaining():
    """
    returns the milk remaining in the machine
    """
    return resources["milk"]


def coffee_remaining():
    """
    returns the coffee remaining in the machine
    """
    return resources["coffee"]


def consume_resources(water, milk, coffee):
    """
    deducts the resources used for making a drink
    :param water: water needed for the drink
    :param water: milk needed for the drink
    :param water: coffee needed for the drink
    """
    resources["water"] = resources["water"] - water
    resources["milk"] = resources["milk"] - milk
    resources["coffee"] = resources["coffee"] - coffee
    return True


def check_resources(name_of_drink):
    """
    checks whether a drink can be prepared with remaining resources
    :param name_of_drink: name of the drink to be prepared
    :returns: True or False
    """
    water_n = water_needed(name_of_drink)
    milk_n = milk_needed(name_of_drink)
    coffee_n = coffee_needed(name_of_drink)

    if water_remaining() - water_n < 0:
        print("Sorry there is not enough water.")
        return False
    if milk_remaining() - milk_n < 0:
        print("Sorry there is not enough milk.")
        return False
    if coffee_remaining() - coffee_n < 0:
        print("Sorry there is not enough coffee.")
        return False

    return True


def add_money(money_to_add):
    global collection
    collection += money_to_add


def process_coins(cost_of_drink):
    """
    returns the water remaining in the machine
    :param cost_of_drink: cost of the drink to be prepared
    :returns True or False
    """
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    total_coin_value = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    print(f"Total coins inserted {total_coin_value}.")
    if total_coin_value == cost_of_drink:
        return True
    elif total_coin_value > cost_of_drink:
        change = round(total_coin_value - cost_of_drink,2)
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print(f"Sorry {total_coin_value} is not enough money. Money Refunded.")
        return False


def get_drink_ready(make_the_drink):
    """
    deducts the resources needed to make a drink
    :param make_the_drink: name of the drink to make
    :returns True
    """
    consume_resources(water_needed(make_the_drink), milk_needed(make_the_drink), coffee_needed(make_the_drink))
    return True


def make_a_drink(drink):
    if check_resources(drink):
        cost = MENU[drink]["cost"]
        print(f"Cost of the drink is {cost}")
        if process_coins(cost):
            add_money(cost)
            if get_drink_ready(drink):
                return True
    return False


def print_report():
    print(f"Water: {water_remaining()}ml")
    print(f"Milk: {milk_remaining()}ml")
    print(f"Coffee: {coffee_remaining()}ml")
    print(f"Money: ${collection}")
    return True


"""
Welcome the user. Offer the choice of our Menu.
"""
continue_operation = True
while continue_operation:
    choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if make_a_drink(choice):
            print(f"Enjoy your {choice}. ☕☕☕")
    elif choice == "report":
        print("Generating a Report...")
        print_report()
    elif choice == "off":
        print("Bye...Byee...🙋‍🙋‍🙋️")
        continue_operation = False
    else:
        print("Choose a correct option!!!😡")
