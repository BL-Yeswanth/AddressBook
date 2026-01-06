from person import Person


class ContactOperations:
    """
    Handles all contact-related operations
    """
    def __init__(self):
        # UC5 Add multiple contacts using list
        self.contacts = []  # This will now store Person objects for UC2

    # =========================
    # UC1: Create Contact (dictionary version)
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

    # =========================
    # UC2: Add Contact (Object-oriented version)
    # =========================
    def add_person_contact(self, person):
        """
        Add a Person object to the AddressBook
        """
        self.contacts.append(person)
        print(f"\nContact {person.first_name} {person.last_name} added successfully.")

    def display_person_contacts(self):
        """
        Display all Person objects in AddressBook
        """
        if not self.contacts:
            print("\nNo contacts in AddressBook.")
            return

        print("\nAddressBook Contacts:")
        for person in self.contacts:
            # Check if it is a dictionary (UC1) or Person object (UC2)
            if isinstance(person, dict):
                print(
                    f"{person['first_name']} {person['last_name']}, "
                    f"{person['address']}, {person['city']}, {person['state']} - {person['zip']}, "
                    f"Phone: {person['phone']}, Email: {person['email']}"
                )
            elif isinstance(person, Person):
                print(
                    f"{person.first_name} {person.last_name}, "
                    f"{person.address}, {person.city}, {person.state} - {person.zip_code}, "
                    f"Phone: {person.phone}, Email: {person.email}"
                )

    # =========================
    # UC3: Edit Contact using Name
    # =========================
    def edit_contact_by_name(self, first_name):
        for contact in self.contacts:
            # UC1 Dictionary contact
            if isinstance(contact, dict) and contact["first_name"].lower() == first_name.lower():
                print(f"\nEditing contact: {contact['first_name']}")
                contact["address"] = input("New Address: ")
                contact["city"] = input("New City: ")
                contact["state"] = input("New State: ")
                contact["zip"] = input("New Zip: ")
                contact["phone"] = input("New Phone: ")
                contact["email"] = input("New Email: ")
                print("\nContact updated successfully.")
                return contact

            # UC2 Person object
            if isinstance(contact, Person) and contact.first_name.lower() == first_name.lower():
                print(f"\nEditing contact: {contact.first_name}")
                contact.address = input("New Address: ")
                contact.city = input("New City: ")
                contact.state = input("New State: ")
                contact.zip_code = input("New Zip: ")
                contact.phone = input("New Phone: ")
                contact.email = input("New Email: ")
                print("\nContact updated successfully.")
                return contact

        print("\nContact not found.")
        
    # =========================
    # UC4: Delete Contact using Name
    # =========================
    def delete_contact_by_name(self, first_name):
        for contact in self.contacts:
            # UC1 dictionary contact
            if isinstance(contact, dict) and contact["first_name"].lower() == first_name.lower():
                self.contacts.remove(contact)
                print(f"\nContact '{first_name}' deleted successfully.")
                return first_name

            # UC2 Person object
            if isinstance(contact, Person) and contact.first_name.lower() == first_name.lower():
                self.contacts.remove(contact)
                print(f"\nContact '{first_name}' deleted successfully.")
                return first_name

        print("\nContact not found.")
