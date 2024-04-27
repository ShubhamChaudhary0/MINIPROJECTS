inventory = {}

def add_item(item_name, quantity):
  if item_name in inventory:
    inventory[item_name] += quantity
  else:
    inventory[item_name] = quantity

def remove_item(item_name, quantity):
  if item_name in inventory:
    if inventory[item_name] >= quantity:
      inventory[item_name] -= quantity
    else:
      raise ValueError(f"Insufficient stock of {item_name}. Only {inventory[item_name]} available.")
  else:
    raise ValueError(f"Item {item_name} not found in inventory.")

def list_inventory():
  if inventory:
    print("Inventory:")
    for item, quantity in inventory.items():
      print(f"{item}: {quantity}")
  else:
    print("Inventory is empty.")


add_item("Shirt", 10)
add_item("Pants", 5)
add_item("Shirt", 3) 

remove_item("Pants", 2)
list_inventory()

try:
  remove_item("Hat", 1)
except ValueError as e:
  print(e)
