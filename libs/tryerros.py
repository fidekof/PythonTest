POPULATION_FOR_COUNTRY = {
    'ECUADOR': '12000000',
    'PERU': '13000000',
    'CHILE': '14000000',
    'BRASIL': '150000000',
    'USA': '100000000'
}


def run():
    option = str(input('Escriba un pais: '))
    while option.lower() != 'exit':
        try:
            data = [(key, value) for key, value in POPULATION_FOR_COUNTRY.items() if key == option.upper()][0]
        except IndexError:
            print('No tenemos la poblacion de ' + option.upper())
        else:
            print('{} tiene {} habitantes'.format(data[0], data[1]))
        finally:
            option = str(input('Escriba un pais: '))


if __name__ == '__main__':
    run()
