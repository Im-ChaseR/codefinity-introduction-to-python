grocery_inventory = {"Milk": ("Dairy", 3.50, 8),
                    "Eggs": ("Dairy", 5.50, 30),
                    "Bread": ("Bakery", 2.99, 15),
                    "Apples": ("Produce", 1.50, 50)}
#price_of_eggs = grocery_inventory["Eggs"][1]
#if price_of_eggs > 5:
    #print("Eggs are too expensive, reducing the price by $1.")
    #grocery_inventory["Eggs"] = ("Dairy", 4.50, 30)

price_of_eggs = grocery_inventory["Eggs"][1]
if price_of_eggs > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    category, _, stock = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"] = (category, price_of_eggs - 1, stock)
else:
    print("The price of eggs is reasonable.")

grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

stock_of_milk = grocery_inventory["Milk"][2]
if stock_of_milk:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    category, price, _ = grocery_inventory["Milk"]
    grocery_inventory["Milk"] = (category, price, stock_of_milk + 20)
else:
    print("Milk has sufficient stock.")

price_of_apples = grocery_inventory["Apples"][1]
if price_of_apples > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print(f"Updated inventory: {grocery_inventory}")
