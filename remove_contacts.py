def remove_contacts(contacts,Name):
        # Remove a contact book Name
        for contact in contacts:
            if contact['Name'] == Name:
                contacts.remove(contact)
                print(f"Contact Book Name  {Name} removed successfully.")
                return
        print(f"No contact found with Name {Name}.")