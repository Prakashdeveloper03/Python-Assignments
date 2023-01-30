import json


def read_data():
    try:
        with open("files/contacts.json", "r") as f:
            return json.load(f)
    except Exception:
        return {}


def add_contact(contacts, name, number):
    contacts[name] = number
    with open("files/contacts.json", "w") as f:
        json.dump(contacts, f)
    print("Contact added successfully!\n")


def search_contact(contacts, name):
    if name in contacts:
        print("Name: ", name)
        print("Number: ", contacts[name])
    else:
        print("Contact not found.\n")


def update_number(contacts, name, new_number):
    if name in contacts:
        contacts[name] = new_number
        with open("files/contacts.json", "w") as f:
            json.dump(contacts, f)
        print("Number updated successfully!\n")
    else:
        print("Contact not found.\n")


def update_name(contacts, name, new_name):
    if name in contacts:
        number = contacts[name]
        del contacts[name]
        contacts[new_name] = number
        with open("files/contacts.json", "w") as f:
            json.dump(contacts, f)
        print("Name updated successfully!\n")
    else:
        print("Contact not found.\n")


def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        with open("files/contacts.json", "w") as f:
            json.dump(contacts, f)
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")


def display_contact(contacts, name=None):
    if name:
        for contact in contacts:
            if contacts["name"] == name:
                print(contact)
                print(contact[name])
                return
        print("Contact not found\n")
    else:
        for contact in contacts:
            print(contact)
        print()


def menu():
    while True:
        print("1. Add new contact")
        print("2. Search contact")
        print("3. Update number")
        print("4. Update name")
        print("5. Delete contact")
        print("6. Exit")
        choice = int(input("Enter your choice : "))
        contacts = read_data()
        if choice == 1:
            name = input("Enter the name : ")
            number = input("Enter the phone number: ")
            add_contact(contacts, name, number)
        elif choice == 2:
            name = input("Enter the name : ")
            search_contact(contacts, name)
        elif choice == 3:
            name = input("Enter the name : ")
            new_number = input("Enter the new number: ")
            update_number(contacts, name, new_number)
        elif choice == 4:
            name = input("Enter the previous name : ")
            new_name = input("Enter the new name: ")
            update_name(contacts, name, new_name)
        elif choice == 5:
            name = input("Enter the name : ")
            delete_contact(contacts, name)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    menu()
