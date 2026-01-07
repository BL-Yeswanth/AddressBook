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
            for book in self.address_books.values()
            for person in book.contacts
            if person.city.lower() == city.lower()
        ]

        self._display_search_results(results)

    # =========================
    # UC8: Search Person by State
    # =========================
    def search_person_by_state(self, state):
        print(f"\nSearching persons in State: {state}")

        results = [
            person
            for book in self.address_books.values()
            for person in book.contacts
            if person.state.lower() == state.lower()
        ]

        self._display_search_results(results)

    # =========================
    # UC9: View Persons by City
    # =========================
    def view_persons_by_city(self):
        city_dict = {}

        for book in self.address_books.values():
            for person in book.contacts:
                city = person.city
                city_dict.setdefault(city, []).append(person)

        print("\nPersons grouped by City:")
        for city, persons in city_dict.items():
            print(f"\nCity: {city}")
            for p in persons:
                print(f"  - {p.first_name} {p.last_name}")

    # =========================
    # UC9: View Persons by State
    # =========================
    def view_persons_by_state(self):
        state_dict = {}

        for book in self.address_books.values():
            for person in book.contacts:
                state = person.state
                state_dict.setdefault(state, []).append(person)

        print("\nPersons grouped by State:")
        for state, persons in state_dict.items():
            print(f"\nState: {state}")
            for p in persons:
                print(f"  - {p.first_name} {p.last_name}")

    # =========================
    # UC10: Count Persons by City
    # =========================
    def count_persons_by_city(self):
        city_count = {}

        for book in self.address_books.values():
            for person in book.contacts:
                city = person.city
                city_count[city] = city_count.get(city, 0) + 1

        print("\nPerson Count by City:")
        for city, count in city_count.items():
            print(f"{city}: {count}")

    # =========================
    # UC10: Count Persons by State
    # =========================
    def count_persons_by_state(self):
        state_count = {}

        for book in self.address_books.values():
            for person in book.contacts:
                state = person.state
                state_count[state] = state_count.get(state, 0) + 1

        print("\nPerson Count by State:")
        for state, count in state_count.items():
            print(f"{state}: {count}")

    # =========================
    # Helper
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
                f"Phone: {person.phone}"
            )
