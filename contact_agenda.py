# Base class for a person
class Persona:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        # Method to represent the person's information as a string
        return f"{self.name} {self.last_name}, {self.age} years old"


# Contact class that inherits from Persona and includes phone and address
class Contacto(Persona):
    def __init__(self, name, last_name, age, phone, address):
        super().__init__(name, last_name, age)
        self.phone = phone
        self.address = address

    def __str__(self):
        # Method to represent the contact's information as a string
        return f"{super().__str__()}, Phone: {self.phone}, Address: {self.address}"


# Agenda class to manage contacts
class Agenda:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        # Method to add a contact to the agenda
        self.contacts.append(contact)
        print(f"Contact {contact.name} added to the agenda.")

    def remove_contact(self, name):
        # Method to remove a contact from the agenda by name
        found_contact = None
        for contact in self.contacts:
            if contact.name == name:
                found_contact = contact
                break
        if found_contact:
            self.contacts.remove(found_contact)
            print(f"Contact {name} removed from the agenda.")
        else:
            print(f"Contact {name} not found in the agenda.")

    def modify_contact(self, name, new_phone=None, new_address=None):
        # Method to modify the phone or address of a contact by name
        for contact in self.contacts:
            if contact.name == name:
                if new_phone:
                    contact.phone = new_phone
                if new_address:
                    contact.address = new_address
                print(f"Contact {name} modified.")
                return
        print(f"Contact {name} not found in the agenda.")

    def search_contact(self, name):
        # Method to search for a contact by name
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def list_contacts(self):
        # Method to list all contacts in the console
        for contact in self.contacts:
            print(contact)


# Decorator to list contacts in HTML format
def html_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        html_result = "<html><body><ul>"
        for contact in result:
            html_result += f"<li>{contact}</li>"
        html_result += "</ul></body></html>"
        return html_result
    return wrapper


# AgendaHTML class that inherits from Agenda and implements the decorated list_contacts_html method
class AgendaHTML(Agenda):
    @html_decorator
    def list_contacts_html(self):
        # Decorated method to list contacts in HTML format
        return [str(contact) for contact in self.contacts]


# Example usage
# Create an instance of AgendaHTML
agenda = AgendaHTML()

# Create two contacts
contact1 = Contacto("John", "Doe", 30, "123456789", "123 Fake St")
contact2 = Contacto("Jane", "Smith", 25, "987654321", "742 Evergreen Terrace")

# Add contacts to the agenda
agenda.add_contact(contact1)
agenda.add_contact(contact2)

# List contacts in HTML format
print(agenda.list_contacts_html())

# Modify a contact's phone number
agenda.modify_contact("John", new_phone="111111111")

# List modified contacts in HTML format
print(agenda.list_contacts_html())

# Remove a contact from the agenda
agenda.remove_contact("Jane")

# List remaining contacts in HTML format
print(agenda.list_contacts_html())
