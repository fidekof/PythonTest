
def protected2(func):
    def wrapper(password):
        if passwor == 'fhalcom':
            return func()
        else:
            print('Contrasena incorrecta')
    return wrapper

@protected2
def protected_func():
    print('Tu contrasena es correcta')

if  __name__ == '__main__':
    passwor = str(input('Ingrese la contrasena: '))
    protected_func(passwor)
