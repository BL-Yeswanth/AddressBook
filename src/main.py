from contact import ContactOperations

class AddressBookMain:
    """
    Entry point of AddressBook Application
    """

    def __init__(self):
        # Future initialization (file paths, config, etc.)
        self.contact_operations = ContactOperations()

    def start(self):
        self.display_welcome_message()
        
        #UC1: Create Contact
        contact = self.contact_operations.create_contact()
        
        print("\nContact Created Successfully")
        
        self.display_contact(contact)

    def display_welcome_message(self):
        print("Welcome to Address Book Program")
        
    def display_contact(self,contact):
        print(
            f"{contact['first_name']} {contact['last_name']}, "
            f"{contact['address']}, {contact['city']}, {contact['state']} - {contact['zip']}, "
            f"Phone: {contact['phone']}, Email: {contact['email']}"
        )

if __name__ == "__main__":
    app = AddressBookMain()
    app.start()
