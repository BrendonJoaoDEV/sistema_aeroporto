while True:
    entrada = input('Digite: ').strip().lower()

    if entrada == '':  # Entrada vazia
        print('Entrada Vazia!')
        input('Pressione qualquer tecla para continuar...')

    elif entrada:  # Decimal
        print('Entrada Decimal!')
        input('Pressione qualquer tecla para continuar...')

    elif entrada:  # Inteiro
        print('Entrada Inteira!')
        input('Pressione qualquer tecla para continuar...')

    elif entrada:  # String
        print('Entrada String!')
        input('Pressione qualquer tecla para continuar...')

    elif entrada:  # Data
        print('')
        input('Pressione qualquer tecla para continuar...')

    elif entrada:  # Hora
        print('')
        input('Pressione qualquer tecla para continuar...')

    elif entrada:  # Data e Hora
        print('')
        input('Pressione qualquer tecla para continuar...')

    elif entrada:  # CPF
        print('Entrada CPF!')
        input('Pressione qualquer tecla para continuar...')

    elif entrada:  # Número de telefone
        print('Entrada número de Telefone!')
        input('Pressione qualquer tecla para continuar...')
    
    # Essa validação tem que ficar por último ou ela sempre
    # retornará sua mensagem quando o usuário entrar com qualquer valor
    elif bool(entrada) == True or bool(entrada) == False:  # Boleano
        print('Entrada Boleana!')
        input('Pressione qualquer tecla para continuar...')

    else:
        print('Tipo de dado não existente!')
        input('Pressione qualquer tecla para continuar...')
