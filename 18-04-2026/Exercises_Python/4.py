#Inventory Management

inventory = {
    "laptop": 10,
    "mouse": 25,
    "keyboard": 15
}

inventory["monitor"] = 8
inventory["laptop"] -= 2

print("Items with stock less than 10:")
for item, stock in inventory.items():
    if stock < 10:
        print(item, "-", stock)