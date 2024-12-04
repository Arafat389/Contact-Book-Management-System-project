import csv
import os

CONTACTS_FILE = "contacts.csv"

def save_contact(contact):
    """Save a single contact to the file."""
    file_exists = os.path.exists(CONTACTS_FILE)
    with open(CONTACTS_FILE, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ["Name", "Email", "Phone_Number", "Address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()
        writer.writerow(contact)
