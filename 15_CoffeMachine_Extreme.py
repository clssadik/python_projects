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

cash = 0

def math(get_choice):
    print("Please insert coins.")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickels = float(input("How many nickels?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    moneysum = quarters + dimes + nickels + pennies
    calculate(moneysum,get_choice)

def decrease(get_sum,calculate_choice):
    global cash
    cash += round(get_sum,3)
    resources["water"] -= MENU[calculate_choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[calculate_choice]["ingredients"]["coffee"]
    resources["milk"] -= MENU[calculate_choice]["ingredients"]["milk"]
    change = round(get_sum - MENU[calculate_choice]["cost"], 2)
    print(f"Here is ${change} in change.")
    print(f"Here is your {calculate_choice} ☕️. Enjoy!")

def statement(get_sum,calculate_choice):
    if resources["water"] >= MENU[calculate_choice]["ingredients"]["water"]:
        if resources["coffee"] >= MENU[calculate_choice]["ingredients"]["coffee"]:
            decrease(get_sum, calculate_choice)
        else:
            print("Sorry, there is not enough coffee..")
    else:
        print("Sorry, there is not enough water.")

def calculate(get_sum,calculate_choice):
    if get_sum >= MENU[calculate_choice]["cost"]:
        if calculate_choice == "espresso":
            statement(get_sum,calculate_choice)

        else:
            if resources["milk"] >= MENU[calculate_choice]["ingredients"]["milk"]:
                statement(get_sum,calculate_choice)
            else:
                print("Sorry, there is not enough milk.")
    else:
        print("Sorry that's not enough money. Money refunded")

flag = True

while flag:
    choice = str(input("What would you like? (espresso/latte/cappuccino): ").lower())
    if choice == "off":
        flag = False
        continue
    if choice ==  "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gr")
        print(f"Money: ${cash}")
        continue
    math(choice)

