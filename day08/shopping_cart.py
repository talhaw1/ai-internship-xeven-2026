"""
Shopping Cart System

Features:
- Add item
- Remove item
- Update quantity
- Calculate total with discount
- Display receipt
"""

# Parallel lists
item_names = []
item_prices = []
item_quantities = []


# 🔹 Add item
def add_item(name, price, quantity):
    item_names.append(name)
    item_prices.append(price)
    item_quantities.append(quantity)
    print(f"{name} added to cart.")


# 🔹 Remove item
def remove_item(name):
    if name in item_names:
        index = item_names.index(name)
        item_names.pop(index)
        item_prices.pop(index)
        item_quantities.pop(index)
        print(f"{name} removed.")
    else:
        print("Item not found.")


# 🔹 Update quantity
def update_quantity(name, new_quantity):
    if name in item_names:
        index = item_names.index(name)
        item_quantities[index] = new_quantity
        print(f"{name} quantity updated.")
    else:
        print("Item not found.")


# 🔹 Calculate total
def calculate_total():
    total = 0
    for i in range(len(item_names)):
        total += item_prices[i] * item_quantities[i]

    # Apply discount
    if total > 100:
        discount = total * 0.10
        total -= discount
        print(f"Discount applied: ${discount:.2f}")

    return total


# 🔹 Display receipt
def display_receipt():
    print("\n--- Receipt ---")
    for i in range(len(item_names)):
        subtotal = item_prices[i] * item_quantities[i]
        print(f"{item_names[i]} | Qty: {item_quantities[i]} | Price: ${item_prices[i]} | Subtotal: ${subtotal}")

    print(f"\nTotal: ${calculate_total():.2f}")


# 🔹 Recently added (last 3 items)
def recently_added():
    print("\nRecently Added Items:", item_names[-3:])


# 🔥 Demo
add_item("Laptop", 800, 1)
add_item("Mouse", 20, 2)
add_item("Keyboard", 50, 1)
add_item("USB Cable", 10, 3)

update_quantity("Mouse", 3)
remove_item("USB Cable")

display_receipt()
recently_added()