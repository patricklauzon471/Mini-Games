# Makes 3 hot flavours
# Each one requires a different quantity of water, coffee, and milk
# Each is a different price

# Steps
# 1. Prompt user by asking what they would like
# 2. Turn off coffee machine by entering off
# 3. Print report when the user enters report
# 4. Check if there are sufficient resources to make the drink
# 5. If there are sufficient resources should prompt the user to insert coins
# 6. Check if the transaction is successful, tell user if too much/not enough moeny has been entered
# 7. Make the coffee

# The name and resources each type of coffee requires
# ingredients are nested in a sperate dictionary and will have to be accessed seperately
Menu = {"espresso": {"ingredients": {"water": 50, "coffee": 18, }, "cost": 1.5, },
        "latte": {"ingredients": {"milk": 150, "coffee": 24, "water": 200, }, "cost": 2.5, },
        "cappucino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24, }, "cost": 3.0, },
        }

# Need to check if there aree resources available to make the coffee
# Variable passed in that will eventually be the ingredients values extracted from the menu


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        # If the resource requires more resources than are available the drink can't be made
        # False is returned which causes the while loop to end and the order to be negated
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

# Function to get the input for how much money the user will pay
# Returns a total after all the change has been added
# Will need another function to determine if the payment is sufficient based on the amount payed and the cost of the drink


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters")) * 0.25
    total += int(input("how many dimes")) * 0.1
    total += int(input("how many nickels")) * 0.05
    total += int(input("how many pennies")) * 0.01
    return total

# Function created to determine the success of the purchase
# Function needs to handle 2 variables based on the cost of the drink from the menu and the total returned in "process coins"


def is_transaction_successful(money_recieved, drink_cost):
    # If the payment is greater or equal to cost the order is succesful and change is returned
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost)
        # Profit is initialized afer this function so it needs to be globalized
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money")
        return False


# Starting resources
resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
profit = 0


# Function to make the coffee if all of the other functions have passed succesfully
# First variable determines the drink while the second is used to recalculate inventory
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True


while is_on:
    choice = input("What would you like? espresso, cappucino, or latte? ")
    # Exit the loop if the coffee machine is turned off
    if choice == "off":
        is_on == False
        # If the user calls for a report format the current resources available
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}ml")
    else:
        drink = Menu[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])
