import datetime

# Calculate book club points earned based on number of books purchased
def calculate_points(books_purchased):
    
    # Calculate number of points earned    
    if books_purchased >= 8:
        return 60
    elif books_purchased >= 6:
        return 30
    elif books_purchased >= 4:
        return 15
    elif books_purchased >= 2:
        return 5
    else:
        return 0

def main():
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    username = "Lindy"
    
    # Print timestamp and username
    print(f"\nBook Club Points")
    print(f"User: {username}")
    print(f"Timestamp: {timestamp}\n")
    
    # Ask for the number of books from the user
    try:
        books_purchased = int(input("Enter the number of books purchased this month: "))
        if books_purchased < 0:
            print("Please enter a non-negative number.")
            return
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    # Calculate points
    points = calculate_points(books_purchased)

    # Display the results
    print(f"Books Purchased: {books_purchased}")
    print(f"Points Earned: {points}")

if __name__ == "__main__":
    main()

