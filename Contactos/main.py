from contact_book import ContactBook
from contact import Contact
def run():
    option = ''
    book = ContactBook()
    while option != 'S':
        option = str(input('**********************\n'
                           '[A]gregar\n'
                           '[E]liminar\n'
                           '[L]istar\n'
                           '[S]alir\n'
                           '***********************\n'
                           'Elija su opcion: '))
        if(option=='A'):
            c = Contact()
            c._name = str(input('Nombre: '))
            c._lastname = str(input('Apellido: '))
            c._phone = str(input('Telefono: '))
            c._email = str(input('Email: '))
            book.add_contact(c)
        elif(option=='L'):
            book.listar()

if __name__ == '__main__':
    run()