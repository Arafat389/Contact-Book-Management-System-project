



def search_contact(contacts):
    name_query = input("Enter the Name to Search: ").strip().lower()
    results = [contact for contact in contacts if contact['Name'].lower() == name_query]
    
    if results:
        print("\n--- Search Results ---")
        for contact in results:
            print(f"Name: {contact['Name']}, Email: {contact['Email']}, Phone_Number: {contact['Phone_Number']}, Address: {contact['Address']}")
    else:
        print("No contact found with the given name.")

    
    



