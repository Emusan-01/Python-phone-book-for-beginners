import contact_01 as con
"""add name and phone number
add another phone number to the same name
view phone directory
view a phone number base on name
delete a phone number"""

contacts = []


def contact_info():
    phone_name = input("Phone name: ")
    phone_number = input("Phone number: ")
    if isinstance(phone_name, str) and not len(phone_number) < 11 and not len(phone_number) > 11:
        contacts.append({"Name": phone_name.capitalize(), "Number 1": phone_number})
        print(f"The name {phone_name.capitalize()} with phone number {phone_number}"
              f" added to your contact successfully!\n")
    else:
        print("Number is less or more than eleven!\n")
        contact_info()


def update_number():
    name_to_add = input("Name to add number: ")
    for index, contact in enumerate(contacts):
        if contact["Name"] == name_to_add.capitalize():
            while True:
                update_number = input("New phone number: ")
                if len(update_number) == 11:
                    while True:
                        old_number = input("Number to replace: ")
                        for key, value in contact.items():
                            if len(update_number) == 11 and value == old_number:
                                agreed = input("Enter (Yes/No): ")
                                if agreed.lower() == "yes":
                                    contacts[index][key] = update_number
                                    print(f'Your contact name {contact["Name"]} got number update from Old Number: {old_number} to New number: {update_number}\n')
                                    con.main()


def add_number():
    name_to_add = input("Name to add number: ")
    for index, contact in enumerate(contacts):
        if contact["Name"] == name_to_add.capitalize():
            phone_numbers = input("Enter phone number: ")
            if len(phone_numbers) == 11:
                print(f"Phone number {phone_numbers} will be added to the name {contact['Name']}")
                agreed = input("Enter (Yes/No): ")
                if agreed.lower() == "yes":
                    new_numer = (len(contact) + 1) - 1
                    contact[f"Number {new_numer}"] = phone_numbers
                    print(f"Phone number {phone_numbers} added successfully!\n")
                else:
                    print("\nPhone number {phone_numbers} couldn't be added to your phonebook\n")
            else:
                    print(f"\nThe phone number {phone_numbers} you're trying to add is less than or more than 11digits\n")
                    con.main()


def view_contact():
    print("Contact list:")
    for no, dictionary in enumerate(contacts, start=1):
        new_dict = str(dictionary)
        format_dict = new_dict.replace("{", " ").replace("}", " ").replace("'", " ")
        print(f"{no}.{format_dict}\n")


def view_name():
    name_in_view = input("Name to view: ")
    for index, contact in enumerate(contacts):
        if name_in_view.capitalize() == contact["Name"]:
            new_view = str(contact)
            format_view = new_view.replace("{", "").replace("}", "").replace("'", "")
            print(f"{format_view}\n")
            con.main()
        else:
            print("No such name exist in your contact list!\n")


def name_update():
    old_name = input("Name to Update: ")
    name_to_add = input("New name: ")
    for index, contact in enumerate(contacts):
        if contact["Name"] == old_name.capitalize():
            contact.update({"Name": name_to_add})
            print(f"The name {old_name.capitalize()} changed to {contact['Name'].capitalize()} successfully!\n")


def delete_contact():
    contact_to_delete = input("Contact to Delete: ")
    for index, contact in enumerate(contacts):
        if contact["Name"] == contact_to_delete.capitalize():
            print(f"Do you want to delete contact name {contact['Name']} from your list?")
            del_input = input("Enter (Y/N): ")
            if del_input.lower() == "y":
                contacts.pop(index)
                print(f"Contact name {contact_to_delete} deleted successfully!\n")
            else:
                print("\n")
                con.main()


def delete_phone():
    number_delete = input("Number to delete: ")
    for index, contact in enumerate(contacts):
        for key, value in contact.items():
            if value == number_delete:
                proceed_input = input("Do you want to proceed? (Y/N): ")
                if proceed_input.lower() == "y":
                    del contacts[index][key]
                    print(f'Phone number deleted successfully!\n')
                    con.main()
            else:
                print("Deletion Canceled!\n")
