import csv
import os

CONTACTS_FILE = "contacts.csv"

def load_contacts():
    """Load contacts from the file."""
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            contacts = [row for row in reader]
    return contacts
