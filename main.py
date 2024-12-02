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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

e_water = MENU["espresso"]["ingredients"]["water"]
e_coffee = MENU["espresso"]["ingredients"]["coffee"]
e_cost = MENU["espresso"]["cost"]

l_water = MENU["latte"]["ingredients"]["water"]
l_coffee = MENU["latte"]["ingredients"]["coffee"]
l_milk = MENU["latte"]["ingredients"]["milk"]
l_cost = MENU["latte"]["cost"]

c_water = MENU["cappuccino"]["ingredients"]["water"]
c_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
c_milk = MENU["cappuccino"]["ingredients"]["milk"]
c_cost = MENU["cappuccino"]["cost"]

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

not_off = True
while not_off:

    coffee_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    money= 0
    if coffee_choice == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")

    elif coffee_choice == "off":
        print("Turning off...")
        not_off = False

    else:

        print("Please insert coins.")
        amount_quarter = float(input("how many quarters?:"))
        amount_dimes = float(input("how many dimes?:"))
        amount_nickles = float(input("how many nickles?:"))
        amount_pennies = float(input("how many pennies?:"))
        money = quarters * amount_quarter + dimes * amount_dimes + nickles * amount_nickles + pennies * amount_pennies

    if coffee_choice == "espresso":
        if water> e_water and coffee > e_coffee and money > e_cost:
            water-= e_water
            coffee-= e_coffee
            money-=e_cost
            print(f"Here is ${round(money, 2)} in change.")
            print("Here is your espresso ☕️. Enjoy!")
        elif water< e_water:
            print("Not enough water")
        elif coffee< e_coffee:
            print("Not enough coffee")
        elif money < e_cost:
            print("Not enough money. Refunded added amount")

    elif coffee_choice == "latte":
        if water> l_water and coffee > l_coffee and money > l_cost :
            water-= l_water
            coffee-= l_coffee
            milk-= l_milk
            money -= l_cost
            print(f"Here is ${round(money, 2)} in change.")
            print("Here is your latte ☕️. Enjoy!")
        elif water< l_water:
            print("Not enough water")
        elif coffee< l_coffee:
            print("Not enough coffee")
        elif money < e_cost:
            print("Not enough money. Refunded added amount")

    elif coffee_choice == "cappuccino":
        if water> c_water and coffee > c_coffee and money > c_cost :
            water-= c_water
            coffee-= c_coffee
            milk-= c_milk
            money -= c_cost
            print(f"Here is ${round(money, 2)} in change.")
            print("Here is your cappuccino ☕️. Enjoy!")
        elif water< c_water:
            print("Not enough water")
        elif coffee< c_coffee:
            print("Not enough coffee")
        elif money < e_cost:
            print("Not enough money. Refunded added amount")