from contact import Contact
class ContactBook:
    def __init__(self):
        self.contact_book = {}

    def add_contact(self, contact):
        self.contact_book[len(self.contact_book)+1] = contact

    def remove_by_code(self, contact_code):
        self.contact_book.pop(contact_code)

    def remove(self, c):
        for k, v in self.contact_book.items():
            finded = True if (c._name == None) else c._name.upper() == v._name.upper()
            finded = finded and True if (c._lastname == None) else c._lastname.upper() == v._lastname.upper()
            finded = finded and True if (c._phone == None) else c._phone.upper() == v._phone.upper()
            finded = finded and True if (c._email == None) else c._email.upper() == v._email.upper()

    def listar(self):
        for k, v in self.contact_book.items():
            print('Codigo: {}'.format(str(k)))
            v.print_contact()