def palindromo(palabra):
    palabra = palabra.replace(' ','').lower()
    palabra_inversa = palabra[::-1]
    if palabra_inversa == palabra:
        return True
    else:
        return False


def run():
    palabra = input('Ingresa una palabra o frase: \n ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')

if __name__ == '__main__':
    run()