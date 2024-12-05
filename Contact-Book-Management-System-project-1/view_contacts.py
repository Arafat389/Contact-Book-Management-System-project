def view_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("No contacts found.")
        return

    print("\nContacts:")
    print("=" * 30)
    for i, contact in enumerate(contacts, 1):
        print(f" Name: {contact['Name']} | Email: {contact['Email']} | Phone_Number: {contact['Phone_Number']} | Address: {contact['Address']}")
    print("=" * 30)
