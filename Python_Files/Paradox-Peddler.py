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
def get_price(pair):
    return pair[1]
for item, price in sorted(dictionary.items(), key=get_price):
    print(f"{item}: {price} coins")