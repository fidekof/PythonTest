from lamp_class import LampClass

def run():
    on_lamp = ''
    lamp = LampClass(True)
    while on_lamp.upper() != 'S':
        on_lamp = str(input(''
                            'Ingrese su opcion: \n'
                            '[p]render\n'
                            '[a]pagar\n'
                            '[s]alir\n'))
        if on_lamp.lower() == 'p':
            lamp.turn_on()
        elif on_lamp.lower() == 'a':
            lamp.turn_off()

if __name__ == '__main__':
    run()