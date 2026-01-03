# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold


def calculate_revenue(prices, quantities_sold):
    revenues = []
    for price, qty in zip(prices,quantities_sold):
        revenue = price * qty
        revenues.append(revenue)
    return revenues
revenues = calculate_revenue(prices,quantities_sold)
def formatted_output(products, revenues):
    revenue_per_product = list(zip(products,revenues))
    for name, rev in sorted(revenue_per_product, key=lambda x: x[0]):
        print(f"{name} has total revenue of ${rev}.")
    return revenue_per_product


revenue_per_product = formatted_output(products, revenues)   


# Example of expected output line (do not remove):
#print(f"{revenues[0]} has total revenue of ${revenues[1]}")