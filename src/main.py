class AddressBookMain:
    """
    Entry point of AddressBook Application
    """

    def __init__(self):
        # Future initialization (file paths, config, etc.)
        pass

    def start(self):
        self.display_welcome_message()

    def display_welcome_message(self):
        print("Welcome to Address Book Program")


if __name__ == "__main__":
    app = AddressBookMain()
    app.start()
