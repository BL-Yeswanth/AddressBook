"""
contact.py
All Address Book use cases will be implemented here
"""

# ================
# UC1: Create Contact
# ================

class ContactOperations:
    """
    handles all contact-related operations
    """
    def __init__(self):
        self.contacts = []
    
    # =========================
    # UC1: Create Contact
    # =========================
    
    def create_contact(self):
        print("\nEnter Contact Details")
        
        contact = {
            "first_name": input("First Name: ").strip(),
            "last_name": input("Last Name: ").strip(),
            "address": input("Address: ").strip(),
            "city": input("City: ").strip(),
            "state": input("State: ").strip(),
            "zip": input("Zip Code: ").strip(),
            "phone": input("Phone Number: ").strip(),
            "email": input("Email: ").strip()
        }
        self.contacts.append(contact)
        return contact