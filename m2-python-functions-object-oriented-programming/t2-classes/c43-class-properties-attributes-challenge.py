#Class Properties & Attributes Challenge

class ContactInfo:
    """Creates an instance of ContactInfo"""
    about = "Contact information for customer"
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def description(self):
        return f"{self.name}: {self.email}"

print(ContactInfo.about)

contact = ContactInfo("dave", "lister@email.com")

print(contact.description()) 