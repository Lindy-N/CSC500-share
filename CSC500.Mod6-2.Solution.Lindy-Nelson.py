import datetime

# Get current timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
username = "Lindy"

# Initial dictionary of property elements
property_listing = {
    "county": "Federal Heights",
    "city": "Denver",
    "street": "Pecos"
}

# Insert new elements
property_listing["bedrooms"] = "3"
property_listing["bathrooms"] = "2"

# Update the "street" element
property_listing["street"] = "84th"

# Remove the "bedrooms" element and save the removed value
removed_bedrooms = property_listing.pop("bedrooms")

# Print the finished dictionary and the removed item
print("\nFinal property listing:", property_listing)
print("Removed item (bedrooms):", removed_bedrooms)

print(f"User: {username}")
print(f"Timestamp: {timestamp}")

