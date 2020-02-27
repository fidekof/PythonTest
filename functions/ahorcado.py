import random

IMAGES = ['''
     
     +****+
     |    |
          |
          |
          |
          
          |
          |
    ##############''', '''
     
     +****+
     |    |
     O    |
          |
          |
          |
          |
    ##############''', '''
     
     +****+
     |    |
     O    |
   /|||\  |
          |
          |
          |
    ##############''', '''
     
     +****+
     |    |
     O    |
   /|||\  |
    ===   |
          |
          |
    ##############''', '''
     
     +****+
     |    |
     O    |
   /|||\  |
    ===   |
    |||   |
          |
    ##############''', '''
     
     +****+
     |    |
     O    |
   /|||\  |
  / === \ |
    |||   |
   _| |_  |
    ##############'''

]


WORDS = [
    'TRANSFORMERS',
    'CAMION',
    'EXISTENCIA',
    'PRESICION',
    'INFLUNCIA',
    'ORDENADOR'
    'MESI',
    'NO HAY LUGAR COMO EL HOGAR'
]



def getWord():
    return WORDS[random.randint(0, len(WORDS))]


def printWord(word):
    if word is not None and len(word) > 0:
            print(word)


def setHiddenWord(letra,word,hidden):
    index = word.find(letra)
    while index >= 0:
        hidden = hidden[:index] + letra[0] + hidden[index + 1:]
        word = word[:index] + '*' + word[index + 1:]
        index = word.find(letra[0])
    return hidden


def run():
    print(' A H O R C A D O S ')
    word = getWord()
    HIDENWORDS = '*' * len(word)
    error = 0
    while error < (len(IMAGES) - 1) and HIDENWORDS.find('*') >= 0:
        letra = str(input('Ingrese una letra de la palabra: ')).upper()
        if word.find(letra) >= 0:
            HIDENWORDS = setHiddenWord(letra, word, HIDENWORDS)
            printWord(HIDENWORDS)
        else:
            print(IMAGES[error])
            error += 1


    if(error > len(IMAGES)-2):
        printWord('P E R D I S T E')
    else:
        print('F E L I C I D A D E S')




if __name__ == '__main__':
    run()