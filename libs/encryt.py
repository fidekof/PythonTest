PHRASE_DIC = {
    'a': 'e',
    'b': 'f',
    'c': 'g',
    'd': 'k',
    'e': 'l',
    'f': 'm',
    'g': 'a',
    'h': 'b',
    'i': 'c',
    'j': 'd',
    'k': 'h',
    'l': 'i',
    'm': 'j',
    'n': 'z',
    'o': 'y',
    'p': 'x',
    'q': 'w',
    'r': 'v',
    's': 'u',
    't': 't',
    'u': 's',
    'v': 'r',
    'w': 'q',
    'x': 'p',
    'y': 'o',
    'z': 'n',
    ' ': '_'
}


def get_options():
    return str(input('***********************************\n'
                     '*  Encriptar/Desencriptar\n'
                     '   1 .- Encryp\n'
                     '   2 .- Decryp\n'
                     '   3 .- Exit\n'
                     '   Elije tu opcion: '))


def f_encrypt(prom):

    encrypt_phrase = ''
    for letter in prom:
        encrypt_phrase = encrypt_phrase + PHRASE_DIC[letter]
    return encrypt_phrase


def f_decrypt(prom):
    decrypt_phrase = ''
    for letter in prom:
        for key, value in PHRASE_DIC.items():
            if value == letter:
                decrypt_phrase += key
                break
    return decrypt_phrase


def run():
    option = ''
    while option != '3':
        option = get_options()
        if option != '3' and (option == '1' or option =='2'):
            prom = str(input('Ingrese su mensaje: '))
            if option == '1':
                print(f_encrypt(prom) + '\n')
            else:
                if option == '2':
                    print(f_decrypt(prom) + '\n')


if __name__ == '__main__':
    run()
