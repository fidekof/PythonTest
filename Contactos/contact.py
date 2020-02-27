class Contact:
    def __init__(self):
        pass

    def __int__(self, name, lastname, phone, email ):
        self._name = name
        self._last_name = lastname
        self._phone = phone
        self._email = email

    def print_contact(self):
        print('Name: {}\n'
              'LastName: {}\n'
              'Phone: {}\n'
              'Email:{}\n\n'.format(self._name, self._lastname, self._phone, self._email))