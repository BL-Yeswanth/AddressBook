from person import Person


class ContactOperations:
    """
    Handles all contact-related operations
    """

    def __init__(self):
        self.contacts = []  # UC5: Collection to store contacts

    # =========================
    # UC7: Duplicate Check Helper
    # =========================
    def _is_duplicate_person(self, person):
        for existing in self.contacts:
            if existing == person:
                return True
        return False

    # =========================
    # UC2 + UC5 + UC7: Add Person
    # =========================
    def add_person_contact(self, person):
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
            print(
                f"{person.first_name} {person.last_name}, "
                f"{person.address}, {person.city}, {person.state} - {person.zip_code}, "
                f"Phone: {person.phone}, Email: {person.email}"
            )

    # =========================
    # UC3: Edit Contact
    # =========================
    def edit_contact_by_name(self, first_name):
        for person in self.contacts:
            if person.first_name.lower() == first_name.lower():
                print(f"\nEditing contact: {person.first_name}")
                person.address = input("New Address: ")
                person.city = input("New City: ")
                person.state = input("New State: ")
                person.zip_code = input("New Zip: ")
                person.phone = input("New Phone: ")
                person.email = input("New Email: ")
                print("\nContact updated successfully.")
                return person

        print("\nContact not found.")

    # =========================
    # UC4: Delete Contact
    # =========================
    def delete_contact_by_name(self, first_name):
        for person in self.contacts:
            if person.first_name.lower() == first_name.lower():
                self.contacts.remove(person)
                print(f"\nContact '{first_name}' deleted successfully.")
                return True

        print("\nContact not found.")
        return False
