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
money = {
    "money": 0,
}
def enough_ingredients(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print("not enough " + item)
            return False
    return True


def askMoney(coffee):
    print("The cost of this drink is $" + str(MENU[coffee]['cost']))
    quarters = int(input("how many quarters are you using to pay?")) * 0.25
    dimes = int(input("how many quarters are you using to pay?")) * 0.10
    nickels = int(input("how many quarters are you using to pay?")) * 0.05

    if quarters + dimes + nickels < MENU[coffee]['cost']:
        print("not enough money.")
    else:
        print("Your change is: $" + (
            str(quarters + dimes + nickels - MENU[coffee]['cost'])) + ". Now making coffee")

def update(coffee):
    menu = MENU[coffee]
    money['money'] += menu['cost']
    for item in resources:
        resources[item] -= menu['ingredients'][item]


def main():

    coffee = input("What would you like? (expresso/latte/cappuccino)?")
    if (coffee == "end"):
        print("machine turning off")
        exit()
    elif coffee == "report":
        print("Water: " + str(resources.get("water")) + "ml")
        print("Milk: " + str(resources.get("milk")) + "ml")
        print("Coffee: " + str(resources.get("coffee")) + "g")
        print("Money: $" + str(money['money']))
    else:
        ingredientsRequired = MENU[coffee]['ingredients']
        if enough_ingredients(ingredientsRequired):
            askMoney(coffee)
            update(coffee)
            print("here is your " + coffee + " enjoy!")
            main()


if __name__ == '__main__':
    main()
