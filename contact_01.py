import contact as con


def main():
    while True:
        print("1. Add contact")
        print("2. Add number to existing contact")
        print("3. View Contact list")
        print("4. Change name")
        print("5. Delete Contact")
        print("6. Delete Phone Number from contact")
        print("7. Update Number")
        print("8. View a Name")
        print("9. Quit")
        print()
        user_choice = input("Choose Option: ")
        print("\n")  
    
        if user_choice == "1":
            con.contact_info()
        elif user_choice == "2":
           if not con.contacts:
               print("Contact is empty, you can't add number!\n")
           else:
               con.add_number()
        elif user_choice == "3":
           if not con.contacts:
               print("Contact is empty, nothing to view!\n")
           else:
               con.view_contact()
        elif user_choice == "4":
            if not con.contacts:
                print("Contact is empty, you can't update any name!\n")
            else:
                con.name_update()
        elif user_choice == "5":
            if not con.contacts:
                print("Contact is empty, nothing to delete!\n")
            else:
                con.delete_contact()
        elif user_choice == "6":
            if not con.contacts:
                print("Contact is empty, no phone number to delete!\n")
            else:
                con.delete_phone()
        elif user_choice == "7":
            if not con.contacts:
                print("Contact is empty, you can't update empty contact!\n")
            else:
                con.update_number()
        elif user_choice == "8":
            if not con.contacts:
                print("Contact list is empty!\n")
            else:
                con.view_name()
        elif user_choice == "9":
            break
        else:
            print("Invalid input. Try again!\n")


if __name__=="__main__":
    
    main()

