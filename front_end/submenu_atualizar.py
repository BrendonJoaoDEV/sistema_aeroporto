# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Brendon João Campos Neves.
# Data: 23/12/2024.
# Módulo onde será definida a função que recebe e trata os dados da opção atualizar do menu principal.

def submenu_2():
    # Importação da função exibir tabela:
    from front_end.exibir_tabela import exibir_tabela
    from front_end.exibir_dados import exibir_dados
    from front_end.limpar_terminal import limpar_terminal
    import sqlite3

    # Criando conexão com banco de daods:
    conexao = sqlite3.connect('banco_dados/bancos_dados.db')
    cursor = conexao.cursor()

    # Declaração de variáveis auxiliares e de retorno:
    opcao = ''
    tabela = ''
    identificador = ''
    informacao = ()
    novos_dados = []
    principal = True  # Flag do looping principal

    # Looping da função:
    while principal:
        limpar_terminal()
        # Menu da função:
        print('<::::::::::> ATUALIZAR <::::::::::>')
        print('0 - Voltar')
        print('1 - Viajante')
        print('2 - Telefone')
        print('3 - Companhia')
        print('4 - Avião')
        print('5 - Passagem')
        print('6 - Rota')

        opcao = input('Digite o número da opção que deseja: ').strip()

        if opcao == '0':
            break

        elif opcao == '1':
            tabela = 'viajante'

            # Looping de atualização:
            while True:
                limpar_terminal()
                # Exibindo a tabela viajante e pedindo para o usuário selecionar um viajante:
                print('<::::::::::> VIAJANTE <::::::::::>')
                exibir_tabela('viajante')

                identificador = input(
                    'Qual o id do viajante que deseja alterar? '
                    ).strip().lower()

                # Consulta SQL para encontrar e trazer os dados do viajante:
                cursor.execute(
                    'SELECT * FROM viajante WHERE id_viajante = ?', 
                    identificador)
                resultado = cursor.fetchone()

                # Verificando se os dados foram encontrados:
                if resultado[0] == int(identificador):
                    # Exibindo os dados do viajante selecionado:
                    exibir_dados(resultado, cursor)

                    # Pedindo os novos dados:
                    nome = input(
                        f'Digite o novo nome ou enter para {resultado[1]}: '
                        ).strip().lower() or resultado[1]

                    cpf = input(
                        f'Digite o novo cpf ou enter para {resultado[2]}: '
                        ).strip().lower() or resultado[2]

                    idade = input(
                        f'Digite a nova idade ou enter para {resultado[3]}: '
                        ).strip().lower() or resultado[3]

                    email = input(
                        f'Digite o novo email ou enter para {resultado[4]}: '
                        ).strip().lower() or resultado[4]

                    # Salvando os novos dados
                    informacao = (nome, cpf, idade, email)
                    novos_dados.append(informacao)
                    informacao = ()

                    # Dando ao usuário a opção de alterar outro viajante
                    opcao = input(
                        'Deseja alterar outro viajante (s/n): '
                        ).strip().lower()
                    if opcao == 's':
                        continue
                    else:
                        principal = False
                        break

                # Informando que o viajante não foi encontrado:
                else:
                    print('Viajante não encontrado!')
                    input = 'Pressione qualquer tecla para continuar...'
                    continue

        elif opcao == '2':
            tabela = 'telefone'

            # Loopin de atualização:
            while True:
                limpar_terminal()
                # Exibindo a tabela telefone e pedindo para o usuário selecionar um telefone:
                print('<::::::::::> TELEFONE <::::::::::>')
                exibir_tabela('telefone')

                identificador = input(
                    'Qual o id do telefone que deseja alterar? '
                    ).strip().lower()

                # Consulta SQL para encontrar e trazer os dados do telefone:
                cursor.execute(
                    'SELECT * FROM telefone WHERE id_telefone = ?', 
                    identificador)
                resultado = cursor.fetchone()

                # Verificando se os dados foram encontrados:
                if resultado[0] == int(identificador):
                    # Exibindo os dados do telefone selecionado:
                    exibir_dados(resultado, cursor)

                    # Pedindo os novos dados:
                    id_viajante = input(
                        f'Digite o novo id do viajante ou enter para 
                        {resultado[1]}: ').strip().lower() or resultado[1]

                    telefone = input(
                        f'Digite o novo telefone ou enter para 
                        {resultado[2]}: ').strip().lower() or resultado[2]

                    # Salvando os novos dados:
                    informacao = (id_viajante, telefone)
                    novos_dados.append(informacao)
                    informacao = ()

                    # Dando ao usuário a opção de alterar outro telefone:
                    opcao = input(
                        'Deseja alterar outro telefone (s/n): '
                        ).strip().lower()
                    if opcao == 's':
                        continue
                    else:
                        principal = False
                        break

                # Informando que o telefone não foi encontrado:
                else:
                    print('Telefone não encontrado!')
                    input = 'Pressione qualquer tecla para continuar...'
                    continue

        elif opcao == '3':
            tabela = 'companhia'

            # Looping de alteração:
            while True:
                limpar_terminal()
                # Exibindo a tabela companhia e pedindo ao usuário para selecionar uma companhia:
                print('<::::::::::> COMPANHIA <::::::::::>')
                exibir_tabela('companhia')

                identificador = input(
                    'Qual o id da companhia que deseja alterar? '
                    ).strip().lower()

                # Consulta SQL para encontrar e trazer os dados da companhia:
                cursor.execute(
                    'SELECT * FROM companhia WHERE id_companhia = ?', 
                    identificador)
                resultado = cursor.fetchone()

                # Verificando se os dados foram encontrados:
                if resultado[0] == int(identificador):
                    # Exibindo os dados da companhia selecionada:
                    exibir_dados(resultado, cursor)

                    # Pedindo os novos dados:
                    nome = input(
                        f'Digite o novo nome da companhia ou enter para 
                        {resultado[1]}').strip().lower() or resultado[1]

                    # Salvando os novos dados:
                    informacao = (nome, )
                    novos_dados.append(informacao)
                    informacao = ()

                    # Dando ao usuário a opção de alterar outra companhia:
                    opcao = input(
                        'Deseja alterar outra companhia (s/n): '
                        ).strip().lower()
                    if opcao == 's':
                        continue
                    else:
                        principal = False
                        break

                # Informando que a companhia não foi encontrada:
                else:
                    print('Companhia não encontrada!')
                    input = 'Pressione qualquer tecla para continuar...'
                    continue

        elif opcao == '4':
            tabela = 'aviao'

            # Looping de alteração:
            while True:
                limpar_terminal()
                # Exibindo a tabela aviao e pedindo ao usuário para selecionar um avião:
                print('<::::::::::> AVIÃO <::::::::::>')
                exibir_tabela('aviao')

                identificador = input(
                    'Qual o id do avião que deseja alterar? ').strip().lower()

                # Consulta SQL para encontrar e trazer os dados do avião:
                cursor.execute(
                    'SELECT * FROM aviao WHERE id_aviao = ?', identificador)
                resultado = cursor.fetchone()

                # Verificando se os dados foram encontrados:
                if resultado[0] == int(identificador):
                    # Exibindo os dados do avião selecionada:
                    exibir_dados(resultado, cursor)

                    # Pedindo os novos dados:

                    id_companhia = input(
                        f'Digite a nova companhia ou enter para 
                        {resultado[1]}: ').strip().lower() or resultado[1]

                    nome = input(
                        f'Digite o novo nome do avião ou enter para 
                        {resultado[2]}: ').strip().lower() or resultado[2]

                    modelo = input(
                        f'Digite o novo modelo do avião ou enter para 
                        {resultado[3]}: ').strip().lower() or resultado[3]

                    fabricacao = input(
                        f'Digite o novo ano de fabricação do avião ou enter 
                        para {resultado[4]}: '
                        ).strip().lower() or resultado[4]

                    voos = input(
                        f'Digite o novo número de voos do avião ou enter para 
                        {resultado[5]}: ').strip().lower() or resultado[5]

                    assentos = input(
                        f'Digite o novo número de assentos do avião ou enter
                        para {resultado[6]}: '
                        ).strip().lower() or resultado[6]

                    # Salvando os novos dados:
                    informacao = (id_companhia, nome, modelo,
                                  fabricacao, voos, assentos)
                    novos_dados.append(informacao)
                    informacao = ()

                    # Dando ao usuário a opção de alterar outro avião:
                    opcao = input(
                        'Deseja alterar outro avião (s/n): ').strip().lower()
                    if opcao == 's':
                        continue
                    else:
                        principal = False
                        break

                # Informando que o avião não foi encontrada:
                else:
                    print('Avião não encontrado!')
                    input = 'Pressione qualquer tecla para continuar...'
                    continue

        elif opcao == '5':
            tabela == 'passagem'

            # Looping de alteração:
            # Exibindo a tabela passagem e pedindo ao usuário para selecionar uma passagem:
            # Consulta SQL para encontrar e trazer os dados da passagem:
            # Verificando se os dados foram encontrados:
            # Exibindo os dados da passagem selecionada:
            # Pedindo os novos dados:
            # Salvando os novos dados:
            # Dando ao usuário a opção de alterar outra passagem:
            # Informando que a passagem não foi encontrada:
        elif opcao == '6':
            tabela = 'rota'

            # Looping de alteração:
            # Exibindo a tabela rota e pedindo ao usuário para selecionar uma rota:
            # Consulta SQL para encontrar e trazer os dados da rota:
            # Verificando se os dados foram encontrados:
            # Exibindo os dados da rota selecionada:
            # Pedindo os novos dados:
            # Salvando os novos dados:
            # Dando ao usuário a opção de alterar outra rota:
            # Informando que a rota não foi encontrada:
        else:
            print('Opção inválida: digite apenas números!')

    conexao.commit()
    conexao.close()

    return tabela, identificador, novos_dados
