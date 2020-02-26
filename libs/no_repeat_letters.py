def exist_no_repeat(repeat):
    for key, value in repeat.items():
        if value[1] == 1:
            print('La primera letra es no repetirse es {} en la posicion  {}'.format(key, value[0]))
            break
    print('No existen caracteres repetidos')



def get_first_no_repeat(phrase):
    repeat = {}
    for idx, letter in enumerate(phrase):
        if repeat.get(letter) == None:
            repeat[letter] = (idx, 1)
        else:
            repeat[letter] = (idx, repeat[letter][1] + 1)
    exist_no_repeat(repeat)



def run():
    phrase = str(input("Escribe tu frase: "))
    while phrase != 'exit':
        get_first_no_repeat(phrase)
        phrase = str(input("Escribe tu frase: "))



if __name__ == '__main__':
    run()