vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")

vegetables.sort()

if "carrots" in vegetables:
    print("Carrots are already in the list.")
else:    
    vegetables.append("carrots")
    vegetables.sort()
if "cucumbers" in vegetables:
    print("Cucumbers are already in the list.")
else:
    vegetables.append("cucumbers")
    vegetables.sort()

print(f"Updated Vegetable Inventory: {vegetables}")