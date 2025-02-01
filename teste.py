try:
    while True:
        entrada = input('Digite: ')

        if entrada == float(entrada):
            print('Entrada Decimal')
            input('Pressione qualquer tecla para continuar...')

        elif entrada == int(entrada):
            print('Entrada Inteira!')
            input('Pressione qualquer tecla para continuar...')

        elif entrada == str:
            print('Entrada String')
            input('Pressione qualquer tecla para continuar...')

        else:
            print('Entrada desconhecida!')
            input('Pressione qualquer tecla para continuar...')
except ValueError:
    print('Xiiiiiiiii')