# Define functions to add, remove, and display contacts
import re


def add_contact(contact_dict):
    """Takes the contact information from the user and adds it to the contact dictionary."""
    first_name = input("First Name: ").title()
    last_name = input("Last Name: ").title()
    phone_number = input("Phone Number (Use this format: ###-###-####): ")
    email_address = input("Email Address: ").lower()
    home_address = input("Home Address: ").capitalize()
    contact_notes = input("Notes: ")

    contact_dict[email_address] = {
        "first name": first_name,
        "last name": last_name,
        "phone number": phone_number,
        "home address": home_address,
        "notes": contact_notes
    }
    print("Contact added.")
    return contact_dict


def delete_contact(contact_dict):
    """Searches for a contact using their unique identifier (email) and deletes it from the contact dictionary."""
    try:
        contact_to_delete = input('Enter the email address of the contact you need to delete: ')
        if contact_to_delete not in contact_dict:
            raise KeyError
        test_email = re.search(r"\b[\w.-]+@[\w.-]+\.\w{2,4}\b", contact_to_delete)
        if not test_email:
            print("Invalid input. Please try again.")
        else:
            contact_dict.pop(contact_to_delete)
            print(contact_dict)
    except KeyError:
        print("That email is not in your contact list.")


def display_contact(contact_dict):
    """Displays a list of all contacts with their unique identifiers."""
    if len(contact_dict) == 0:
        raise Exception("No contacts to list.")
    for contact in contact_dict:
        print(f"{contact}: {contact_dict[contact]}")


def main(user_choice, contact_dict):
    """If the user_choice is not 8 or Quit, checks the number and performs the appropriate function."""
    if user_choice == "1" or user_choice == "add a contact":
        add_contact(contact_dict)
    elif user_choice == "2" or user_choice == "delete a contact":
        delete_contact(contact_dict)
    elif user_choice == "3" or user_choice == "display all contacts":
        display_contact(contact_dict)
    else:
        print("Invalid input. Please try again.")

