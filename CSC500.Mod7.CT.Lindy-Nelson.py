import datetime

# Get the current timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
username = "Lindy"

# Print a welcome message with the timestamp and username
print(f"\nCourse Directory")
print(f"User: {username}")
print(f"Timestamp: {timestamp}")
    
# Dictionaries for course details
course_rooms = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411
}

course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Function to get a valid course input
def get_valid_course():
    while True:
        course_number = input("\nEnter a course number: ").strip().upper()
        if course_number in course_rooms:
            return course_number
        else:
            print("Error: Course number not found. Please try again.")

# Function to display course details
def display_course_details(course_number):
    print("\nCourse Details:")
    print(f"Room Number: {course_rooms[course_number]}")
    print(f"Instructor: {course_instructors[course_number]}")
    print(f"Meeting Time: {course_times[course_number]}")

# Function to display timestamp and signature
def display_signature():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nTimestamp: {timestamp}")
    print("Signed by: Lindy")
    
# Main program loop
while True:
    course_number = get_valid_course()
    display_course_details(course_number)
    display_signature()

    # Menu for next action
    while True:
        choice = input("\nEnter 'C' to input another course or 'Q' to quit: ").strip().upper()
        if choice == 'C':
            break  # Loop back to enter a new course
        elif choice == 'Q':
            print("\nExiting Course Directory. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter 'C' or 'Q'.")
