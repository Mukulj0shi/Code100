
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True


while is_on:
    chose_drink = input(f"What would you like to have {menu.get_items()}")
    if chose_drink == "report":
        coffee_maker.report()
        money_machine.report()
    elif chose_drink == "off":
        is_on = False
    else:
        ordered_drink = menu.find_drink(chose_drink)
        if coffee_maker.is_resource_sufficient(ordered_drink) and money_machine.make_payment(ordered_drink.cost):
            coffee_maker.make_coffee(ordered_drink)












"""
drink_menu = order_type_object.get_items()
#print(drink_menu)
drink = input(f"What would you like to have ? {drink_menu} :")
get_drink_info = order_type_object.find_drink(drink)
print(get_drink_info)


report_of_ingredients = report_object.report()
resource_availability = report_object.is_resource_sufficient(get_drink_info)
print(resource_availability)
#prepare_coffee = report_object.make_coffee(get_drink_info)


paid_amount = pay_object.process_coins()
check_amount = pay_object.make_payment(paid_amount)
report_object.report()
pay_object.report()

"""