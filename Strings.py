def factorial(number):
    if number == 0:
        return 1
    else:
        return (number * factorial(number-1))


def run():
    number = 0
    while number<=100:
        number = int(input('Ingrese sus numero: '))
        print('El factorial de {} es {}'.format(number, factorial(number)))



if __name__ == '__main__':
    run()
