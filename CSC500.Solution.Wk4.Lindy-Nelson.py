import datetime

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        "Container with item name, price, and quantity."
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        "Print item name, quantity, price per unit, and total cost."
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ {self.item_price} = ${total_cost}")


def main():
    username = "Lindy"
    start_time = datetime.datetime.now()
    print(f"Execution started at: {start_time} | User: {username}")

    print("\nItem 1")
    name1 = input("Enter the item name: ")
    price1 = float(input("Enter the item price: "))
    quantity1 = int(input("Enter the item quantity: "))
    item1 = ItemToPurchase(name1, price1, quantity1)

    print("\nItem 2")
    name2 = input("Enter the item name: ")
    price2 = float(input("Enter the item price: "))
    quantity2 = int(input("Enter the item quantity: "))
    item2 = ItemToPurchase(name2, price2, quantity2)

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print(f"\nTotal: ${total_cost}")

    end_time = datetime.datetime.now()
    print(f"\nExecution ended at: {end_time} | User: {username}")
    print(f"Total execution time: {end_time - start_time}")


if __name__ == "__main__":
    main()