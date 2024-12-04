from save_contact import save_contact

def add_contact(contacts):
    """Add a new contact."""
    try:
        Name = str((input("Enter Name: ")))
    except Exception as e:
        print(e)   

    Email = input("Enter Email: ")

    try:
        Phone_Number = int((input("Enter Phone: ")))
    except Exception as e:
        print(e)    
    finally:
     
     print("execution complete")

    Address = input("Enter address: ")
    
    # Prevent Duplicate Numbers

    if any(contact["Phone_Number"] == Phone_Number for contact in contacts):
        print("\nError: A contact with this phone number already exists.")
        return 
    
    contact = {
        "Name": Name,
        "Email": Email,
        "Phone_Number": Phone_Number,
        "Address": Address
        
    }

    contacts.append(contact)
    save_contact(contact)
    print("Contact added successfully!")
    return contacts
