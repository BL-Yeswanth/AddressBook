from contact import ContactOperations
from person import Person  # Import your UC2 Person class

class AddressBookMain:
    """
    Entry point of AddressBook Application
    """

    def __init__(self):
        # Initialize AddressBook operations
        self.contact_operations = ContactOperations()

    def start(self):
        self.display_welcome_message()

        # =========================
        # UC1: Create Contact (Dictionary version)
        # =========================
        contact = self.contact_operations.create_contact()
        if contact:
            print("\nContact Created Successfully")
            self.display_contact(contact)

        # =========================
        # UC2: Add Contact using Person class (OOP version)
        # =========================
        print("\nAdd another Contact using Person class")
        person = Person(
            input("First Name: ").strip(),
            input("Last Name: ").strip(),
            input("Address: ").strip(),
            input("City: ").strip(),
            input("State: ").strip(),
            input("Zip Code: ").strip(),
            input("Phone Number: ").strip(),
            input("Email: ").strip()
        )

        # UC2: Add Person object to AddressBook
        self.contact_operations.add_person_contact(person)

        # Display all contacts (both UC1 and UC2)
        self.contact_operations.display_person_contacts()
        
        # UC3: Edit Contact
        print("\n=== Edit Existing Contact ===")
        name = input("Enter First Name to edit: ").strip()
        self.contact_operations.edit_contact_by_name(name)


    def display_welcome_message(self):
        print("Welcome to Address Book Program")

    def display_contact(self, contact):
        print(
            f"{contact['first_name']} {contact['last_name']}, "
            f"{contact['address']}, {contact['city']}, {contact['state']} - {contact['zip']}, "
            f"Phone: {contact['phone']}, Email: {contact['email']}"
        )

    

if __name__ == "__main__":
    app = AddressBookMain()
    app.start()
