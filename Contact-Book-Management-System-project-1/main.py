from load_contacts import load_contacts
from add_contact import add_contact
from view_contacts import view_contacts
import remove_contacts
import search_contacts
def main():
    """Main function to run the contact manager."""
    contacts = load_contacts()
    print("Welcome to Contact Manager!")

    while True:
        print("Contact Book Management System")
        print("0. Exit")
        print("1. Add Contact and Prevent Duplicate Numbers not allow")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Remove Contacts")
        

        menu = input("Select any number: ")

        if menu == '0':
            print("Exiting Contact Book Management System. Goodbye!")
            break

        elif menu == '1':
            add_contact(contacts)

        elif menu == '2':
            view_contacts(contacts)


        elif menu == '3':
            search_contacts.search_contact(contacts) 

        elif menu == '4':
             Name = input("Enter Name Remove: ")
             remove_contacts.remove_contacts(contacts,Name)
        




        else:
            print("Invalid number. Please try again.")

if __name__ == "__main__":
    main()
