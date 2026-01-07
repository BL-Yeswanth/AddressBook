class Person:
    """
    Represents a contact person
    """
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    # =========================
    # UC7: Duplicate Check
    # =========================
    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return (
            self.first_name.lower() == other.first_name.lower()
            and self.last_name.lower() == other.last_name.lower()
        )

    def __hash__(self):
        return hash((self.first_name.lower(), self.last_name.lower()))
