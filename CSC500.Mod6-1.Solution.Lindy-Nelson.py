# Initial list of cheeses
cheeses = ["Gouda", "Cheddar", "Jarlsberg"]

# Insert "Swiss" into the list
cheeses.insert(3, "Swiss")

# Update index 1 to "mozzarella"
cheeses[1] = "mozzarella"

# Remove "Jarlsberg" and save the removed item
removed_cheese = cheeses.pop(2)

# Print the final list and the removed item
print("Final list of cheeses:", cheeses)
print("Removed cheese:", removed_cheese)