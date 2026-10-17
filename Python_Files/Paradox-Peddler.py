money = 100

dictionary  = {
        "Amber with insects": 10, # Cheap items due to abundance
        "Giant egg": 15,
        "Fossilized bone": 8,
        "Prehistoric plant": 5,
        "Lighter" : 120, # Expensive items due to rarity
        "Medicine" : 150,
        "Flashlight" : 100,
        "Metal tools" : 130,
}

# Prints the era and the amount of money the player has
print(f"Era: Dinosaur Age\nMoney: {money}") 
print() # Adds a blank line for better readability
print("Items available for purchase:")
print() # Adds a blank line for better readability
def get_price(pair): # Defines a function to get the price of an item for sorting purposes
    return pair[1]
for item, price in sorted(dictionary.items(), key=get_price):
    print(f"{item}: {price} coins") # Prints the items and their prices in ascending order
choice = input("\nWhat would you like to buy? (Type the item name): ") # Inputs the item the player wants to buy
if choice in dictionary:
    print(f"You have chosen to buy {choice} for {dictionary[choice]} coins.") # Confirms the player's choice
else:
    print("Sorry, that item is not available for purchase, or not for sale here.") # Informs the player if the item is not available
