# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
print(inventory)
print("Stock Processing Started...")
for item in inventory:
    current_stock, min_stock, restock_amount, on_sale = inventory[item]
    print(f"Processing {item}")
    #restocking
    while current_stock < min_stock:
        current_stock += restock_amount
    inventory[item][0] = current_stock
    if current_stock > discount_threshold:
        inventory[item][3] = True
    print("Processing completed")
print(inventory)