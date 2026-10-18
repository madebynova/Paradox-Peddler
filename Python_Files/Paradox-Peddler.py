import os
# Variables
money = 100 # Starting money for the player

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

print("Welcome to the Paradox Peddler!") # Welcomes the player to the game
input("\nPress Enter to start your adventure in the Dinosaur Age...") # Prompts the player to start the game
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console for better readability
# Main game loop
while True:
# Prints the era and the amount of money the player has
        print(f"Era: Dinosaur Age\nMoney: {money}") 
        print() # Adds a blank line for better readability
        print("Items available for purchase:")
        print() # Adds a blank line for better readability
        def get_price(pair): # Defines a function to get the price of an item for sorting purposes
                return pair[1]
        sorted_items = sorted(dictionary.items(), key=get_price) # Sorts the items in the dictionary by price in ascending order
        for number, (item, price) in enumerate(sorted_items, start=1):
            print(f"{number}. {item}: {price} coins") # Prints the items and their prices in ascending order
        try:
            choice = int(input("\nWhat would you like to buy? (Enter the item number): ")) # Inputs the item the player wants to buy
        except ValueError:
                choice = 0
        os.system('cls' if os.name == 'nt' else 'clear') # Clears the console for better readability
        if 1 <= choice <= len(sorted_items):
                item, price = sorted_items[choice - 1]
                if money >= price: # Checks if the player has enough money to buy the item
                        money -= price # Deducts the price of the item from the player's money
                        print(f"You have chosen to buy {item} for {price} coins.") # Confirms the player's choice
                        print(f"Remaining money: {money}") # Shows the player how much money they have left
                else:
                        print("You don't have enough money to buy that item.") # Informs the player if the item is not available for purchase
        else:
                print("Invalid choice. Please select a valid item number.") # Informs the player if they entered an invalid item number
        print() # Adds a blank line for better readability
