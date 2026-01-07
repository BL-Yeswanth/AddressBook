from contact import ContactOperations
from person import Person


class AddressBookSystem:
    """
    UC6: Manages multiple Address Books
    """
    def __init__(self):
        # Dictionary: AddressBookName -> ContactOperations
        self.address_books = {}

    def create_address_book(self, name):
        if name in self.address_books:
            print("\nAddress Book already exists.")
        else:
            self.address_books[name] = ContactOperations()
            print(f"\nAddress Book '{name}' created successfully.")

    def get_address_book(self, name):
        return self.address_books.get(name)

    def display_address_books(self):
        if not self.address_books:
            print("\nNo Address Books available.")
            return

        print("\nAvailable Address Books:")
        for name in self.address_books:
            print(f"- {name}")

    # =========================
    # UC8: Search Person by City
    # =========================
    def search_person_by_city(self, city):
        print(f"\nSearching persons in City: {city}")

        results = [
            person
            for address_book in self.address_books.values()
            for person in address_book.contacts
            if isinstance(person, Person)
            and person.city.lower() == city.lower()
        ]

        self._display_search_results(results)

    # =========================
    # UC8: Search Person by State
    # =========================
    def search_person_by_state(self, state):
        print(f"\nSearching persons in State: {state}")

        results = [
            person
            for address_book in self.address_books.values()
            for person in address_book.contacts
            if isinstance(person, Person)
            and person.state.lower() == state.lower()
        ]

        self._display_search_results(results)

    # =========================
    # UC8: Helper Method
    # =========================
    def _display_search_results(self, results):
        if not results:
            print("No matching persons found.")
            return

        print("\nSearch Results:")
        for person in results:
            print(
                f"{person.first_name} {person.last_name}, "
                f"{person.city}, {person.state}, "
                f"Phone: {person.phone}, Email: {person.email}"
            )
