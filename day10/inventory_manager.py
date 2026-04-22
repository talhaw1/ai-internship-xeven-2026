"""
Product Inventory Manager using Nested Dictionaries + JSON
"""

import json

# Main inventory dictionary
inventory = {}


# 🔹 Add Product
def add_product(product_id, name, price, quantity, category):
    if product_id in inventory:
        print("Product already exists.")
    else:
        inventory[product_id] = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "category": category
        }
        print(f"Product {name} added.")


# 🔹 Update Stock
def update_stock(product_id, quantity):
    if product_id in inventory:
        inventory[product_id]["quantity"] += quantity
        print(f"Stock updated for {inventory[product_id]['name']}")
    else:
        print("Product not found.")


# 🔹 Search by Category
def search_by_category(category):
    result = []

    for pid, details in inventory.items():
        if details["category"] == category:
            result.append((pid, details))

    return result


# 🔹 Low Stock Alert
def low_stock_alert(threshold=5):
    low_stock_items = []

    for pid, details in inventory.items():
        if details["quantity"] <= threshold:
            low_stock_items.append((pid, details))

    return low_stock_items


# 🔹 Total Inventory Value
def total_inventory_value():
    total = 0

    for details in inventory.values():
        total += details["price"] * details["quantity"]

    return total


# 🔹 Average Price per Category
def average_price_per_category():
    category_data = {}

    for details in inventory.values():
        cat = details["category"]

        if cat not in category_data:
            category_data[cat] = []

        category_data[cat].append(details["price"])

    avg_prices = {}

    for cat, prices in category_data.items():
        avg_prices[cat] = sum(prices) / len(prices)

    return avg_prices


# 🔹 Save to JSON
def save_inventory(filename="inventory.json"):
    with open(filename, "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved to JSON.")


# 🔹 Load from JSON
def load_inventory(filename="inventory.json"):
    global inventory

    try:
        with open(filename, "r") as file:
            inventory = json.load(file)
        print("Inventory loaded successfully.")
    except FileNotFoundError:
        inventory = {}
        print("No existing inventory found.")


# 🔥 DEMO EXECUTION

load_inventory()

add_product("P1", "Laptop", 1000, 5, "Electronics")
add_product("P2", "Phone", 500, 10, "Electronics")
add_product("P3", "Chair", 100, 3, "Furniture")

update_stock("P3", 2)

print("\nElectronics Products:", search_by_category("Electronics"))

print("\nLow Stock Items:", low_stock_alert())

print("\nTotal Inventory Value:", total_inventory_value())

print("\nAverage Price per Category:", average_price_per_category())

save_inventory()