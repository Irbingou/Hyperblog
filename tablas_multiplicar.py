def run():
    for numero1 in range(1, 11):
        print(f'Esta es la tabla del {numero1}')
        for numero2 in range(1, 11):
            print(f'{numero1} * {numero2} es igual a: {numero1 * numero2}')

if __name__ == '__main__':
    run()