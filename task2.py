import json

FILE_NAME = "contacts.json"


# LOAD CONTACTS FROM JSON FILE
def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


# SAVE CONTACTS TO JSON FILE
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# ADD CONTACT
def add_contact(contacts):

    name = input("Enter Name: ")
    phone = input("Enter Phone: ")

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)

    save_contacts(contacts)

    print("Contact Added Successfully")


# VIEW CONTACTS
def view_contacts(contacts):

    if len(contacts) == 0:
        print("No Contacts Found")

    else:
        print("\n--- CONTACT LIST ---")

        for contact in contacts:
            print(f"Name : {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print("-------------------")


# SEARCH CONTACT
def search_contact(contacts):

    search_name = input("Enter Name to Search: ")

    found = False

    for contact in contacts:

        if contact["name"].lower() == search_name.lower():

            print("Contact Found")
            print(f"Phone: {contact['phone']}")

            found = True
            break

    if not found:
        print("Contact Not Found")


# DELETE CONTACT
def delete_contact(contacts):

    delete_name = input("Enter Name to Delete: ")

    found = False

    for contact in contacts:

        if contact["name"].lower() == delete_name.lower():

            contacts.remove(contact)

            save_contacts(contacts)

            print("Contact Deleted")

            found = True
            break

    if not found:
        print("Contact Not Found")


# MAIN PROGRAM
def main():

    contacts = load_contacts()

    while True:

        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            print("Exiting Contact Book")
            break

        else:
            print("Invalid Choice")


# RUN PROGRAM
main()