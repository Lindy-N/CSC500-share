import datetime

# Calculate rainfall over a period of years
def rainfall_calculator():
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    username = "Lindy"

    # Print timestamp and username
    print(f"\nRainfall Calculator")
    print(f"User: {username}")
    print(f"Timestamp: {timestamp}\n")

    # Ask user for the number of years
    years = int(input("Enter the number of years: "))

    # Initialize variable for total rainfall and variable for months count
    total_rainfall = 0
    total_months = 0

    # List of month names
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # Outer loop for each year
    for year in range(1, years + 1):
        print(f"\nYear {year}")
        # Inner loop for each of 12 months
        for month_index in range(12):
            while True:
                try:
                    # Get rainfall for the current month
                    rainfall = float(input(f"Enter the inches of rainfall for {months[month_index]}: "))
                    if rainfall < 0:
                        print("Rainfall amount cannot be negative. Please enter a valid value.")
                        continue
                    total_rainfall += rainfall
                    break
                except ValueError:
                    print("Invalid amount. Please enter a numerical value.")
        total_months += 12

    # Calculate average rainfall amount
    average_rainfall = total_rainfall / total_months

    # Display results
    print("\nRainfall Summary")
    print(f"User: {username}")
    print(f"Timestamp: {timestamp}")
    print(f"Total months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

# Run the program
rainfall_calculator()
