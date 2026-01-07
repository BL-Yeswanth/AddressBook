from person import Person
from address_book_system import AddressBookSystem


class AddressBookMain:
    """
    Entry point of AddressBook Application
    """

    def __init__(self):
        self.system = AddressBookSystem()

    def start(self):
        print("Welcome to Address Book Program")

        # =========================
        # UC6: Create / Select Address Book
        # =========================
        while True:
            print("\n1. Create Address Book")
            print("2. Select Address Book")
            choice = input("Choose option (1/2): ").strip()

            if choice == "1":
                book_name = input("Enter New Address Book Name: ").strip()
                self.system.create_address_book(book_name)
                address_book = self.system.get_address_book(book_name)
                break

            elif choice == "2":
                self.system.display_address_books()
                book_name = input("Enter Address Book Name: ").strip()
                address_book = self.system.get_address_book(book_name)

                if not address_book:
                    print("Address Book not found.")
                    continue
                break
            else:
                print("Invalid choice.")

        # =========================
        # UC1: Create Contact (Dictionary)
        # =========================
        contact = address_book.create_contact()
        if contact:
            print("\nContact Created Successfully")

        # =========================
        # UC2 + UC5 + UC7: Add Multiple Contacts (Person)
        # =========================
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

            # UC7 duplicate handled internally
            address_book.add_person_contact(person)

            choice = input("\nAdd another contact? (yes/no): ").strip().lower()
            if choice != "yes":
                break

        # =========================
        # Display All Contacts
        # =========================
        address_book.display_person_contacts()

        # =========================
        # UC3: Edit Contact
        # =========================
        name = input("\nEnter First Name to edit: ").strip()
        address_book.edit_contact_by_name(name)

        # =========================
        # UC4: Delete Contact
        # =========================
        name = input("\nEnter First Name to delete: ").strip()
        address_book.delete_contact_by_name(name)

        # =========================
        # Final Display
        # =========================
        address_book.display_person_contacts()


if __name__ == "__main__":
    app = AddressBookMain()
    app.start()
