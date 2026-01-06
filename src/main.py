from contact import ContactOperations
from person import Person


class AddressBookMain:
    """
    Entry point of AddressBook Application
    """

    def __init__(self):
        self.contact_operations = ContactOperations()

    def start(self):
        self.display_welcome_message()

        # =========================
        # UC1: Create Contact (Dictionary)
        # =========================
        contact = self.contact_operations.create_contact()
        if contact:
            print("\nContact Created Successfully")
            self.display_contact(contact)

        # =========================
        # UC2 + UC5: Add Multiple Contacts using Person class
        # =========================
        print("\nAdd Contacts using Person class")

        while True:
            print("\nEnter Person Details")

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

            self.contact_operations.add_person_contact(person)
            # UC5: Add Multiple Contacts
            choice = input("\nDo you want to add another contact? (yes/no): ").strip().lower()
            if choice != "yes":
                break

        # =========================
        # Display All Contacts
        # =========================
        self.contact_operations.display_person_contacts()

        # =========================
        # UC3: Edit Contact
        # =========================
        print("\n=== Edit Existing Contact ===")
        name = input("Enter First Name to edit: ").strip()
        self.contact_operations.edit_contact_by_name(name)

        # =========================
        # UC4: Delete Contact
        # =========================
        print("\n=== Delete Contact ===")
        name = input("Enter First Name to delete: ").strip()
        self.contact_operations.delete_contact_by_name(name)

        # =========================
        # Final Display
        # =========================
        self.contact_operations.display_person_contacts()

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
