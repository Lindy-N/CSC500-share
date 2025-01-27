class ItemToPurchase:
    def __init__(self, name="", description="", price=0.0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 26, 2025"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify):
        item_found = False
        for item in self.cart_items:
            if item.name == item_to_modify.name:
                if item_to_modify.description != "":
                    item.description = item_to_modify.description
                if item_to_modify.price != 0.0:
                    item.price = item_to_modify.price
                if item_to_modify.quantity != 0:
                    item.quantity = item_to_modify.quantity
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.price * item.quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart")
        print(self.current_date)
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            total_cost = 0
            for item in self.cart_items:
                total_cost += item.price * item.quantity
                print(f"{item.name} {item.quantity} @ ${item.price:.2f} = ${item.price * item.quantity:.2f}")
            print(f"Total: ${total_cost:.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart Descriptions")
        print(self.current_date)
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

def print_menu(cart):
    options = {
        'a': "Add item to cart",
        'r': "Remove item from cart",
        'c': "Change item quantity",
        'i': "Output items' descriptions",
        'o': "Output shopping cart",
        'q': "Quit"
    }
    while True:
        print("\nMENU")
        for key, value in options.items():
            print(f"{key} - {value}")
        choice = input("Choose an option: ")
        
        if choice == 'a':
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = float(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(name, description, price, quantity)
            cart.add_item(item)
        elif choice == 'r':
            name = input("Enter the item name to remove: ")
            cart.remove_item(name)
        elif choice == 'c':
            name = input("Enter the item name to modify: ")
            description = input("Enter the new description (leave blank to keep current): ")
            price = input("Enter the new price (leave blank to keep current): ")
            quantity = input("Enter the new quantity (leave blank to keep current): ")
            price = float(price) if price else 0.0
            quantity = int(quantity) if quantity else 0
            item = ItemToPurchase(name, description, price, quantity)
            cart.modify_item(item)
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    cart = ShoppingCart("Jane Doe", "January 26, 2025")
    print_menu(cart)
