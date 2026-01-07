from person import Person


class ContactOperations:
    """
    Handles all contact-related operations
    """
    def __init__(self):
        self.contacts = []  # UC5: Collection to store contacts

    # =========================
    # UC1: Create Contact (Dictionary)
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
    # UC7: Duplicate Check Helper
    # =========================
    def _is_duplicate_person(self, person):
        for existing in self.contacts:

            # Case 1: Existing contact is Person
            if isinstance(existing, Person) and existing == person:
                return True

            # Case 2: Existing contact is Dictionary (UC1)
            if isinstance(existing, dict):
                if (
                    existing["first_name"].strip().lower() == person.first_name.lower()
                    and existing["last_name"].strip().lower() == person.last_name.lower()
                ):
                    return True

        return False

    # =========================
    # UC2 + UC7: Add Person with Duplicate Check
    # =========================
    def add_person_contact(self, person):
        """
        Add a Person object to AddressBook
        Duplicate check based on first_name + last_name
        """

        if self._is_duplicate_person(person):
            print(
                f"\nDuplicate Entry ❌ : "
                f"{person.first_name} {person.last_name} already exists."
            )
            return False

        self.contacts.append(person)
        print(
            f"\nContact {person.first_name} {person.last_name} added successfully ✅"
        )
        return True

    # =========================
    # Display Contacts
    # =========================
    def display_person_contacts(self):
        if not self.contacts:
            print("\nNo contacts in AddressBook.")
            return

        print("\nAddressBook Contacts:")
        for person in self.contacts:
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
    # UC3: Edit Contact
    # =========================
    def edit_contact_by_name(self, first_name):
        for contact in self.contacts:
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
    # UC4: Delete Contact
    # =========================
    def delete_contact_by_name(self, first_name):
        for contact in self.contacts:
            if isinstance(contact, dict) and contact["first_name"].lower() == first_name.lower():
                self.contacts.remove(contact)
                print(f"\nContact '{first_name}' deleted successfully.")
                return True

            if isinstance(contact, Person) and contact.first_name.lower() == first_name.lower():
                self.contacts.remove(contact)
                print(f"\nContact '{first_name}' deleted successfully.")
                return True

        print("\nContact not found.")
        return False
