"""
Task 1: Contact List Manager
    - Problem Statement: Create a Python script using a custom module to manage a contact list. The script should allow adding, removing, and displaying contacts stored in a list.
    - Expected Outcome: Your script should be able to add new contacts, remove existing contacts, and display all contacts. Each contact can be a dictionary with a name and phone number.
"""
# Implement the logic to interact with the contact manager.
import contact_manager
from datetime import datetime, date
import re

app_is_on = True
contacts = {}
print("Welcome to the Contact Management System!")
while app_is_on:
    menu = "Menu:\n1. Add a new contact\n2. Delete a Contact\n3. Display All Contacts"
    print(menu)
    user_input = input("Choose a number from the menu: ").lower()

    # Check if user wants to quit first. If input = 8 or "quit", application should end.
    contact_manager.main(user_input, contacts)
    # Ask user if they want to do something else with the application. If yes, go back to the top of the loop and display the menu again. If not, end the application.
    another_task = input("\nDo you need anything else? Y or N: ").lower()
    if another_task == "y":
        app_is_on = True
    elif another_task == "n":
        app_is_on = False
    else:
        print("Invalid Input. Please try again.")

"""
Task 2: Date Extractor
    - Problem Statement: Write a Python program that uses the datetime module to extract and display the current month and year. Additionally, allow the user to input a date string and parse it into a datetime object.
    - Expected Outcome: The program should accurately display the current month and year and successfully convert a user-input date string (e.g., "2023-03-15") into a datetime object, handling any invalid inputs gracefully.
"""
# Implement code to display the current month and year
today = date.today()
month = today.strftime('%B')
print(today)
print(f"Current Month: {month}")
print(f"Current Year: {today.year}")
# Implement code to parse a user-input date string into a datetime object
user_date = input("Enter a date in this format: YYYY-MM-DD: ")
valid_date = re.search(r"\d{4}-\d{2}-\d{2}", user_date)
if valid_date:
    date_input = date.fromisoformat(user_date)
    print(type(date_input))
else:
    print("Invalid input.")
