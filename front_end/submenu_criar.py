# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Autor: Brendon João Campos Neves.
# Data: 11/12/2024.
# Módulo onde será definida a função que recebe e trata os dados da opção criar do menu principal.

# Definição da função:
def submenu_criar():
    """Submenu Criar

    Returns:
        string: nome da tabela para uso da função back_end.criar.
        tupla: dados para uso da função back_end.criar.
    """    
    
    # Importação de módulos:
    from front_end.exibir_tabela import exibir_tabela
    from front_end.limpar_terminal import limpar_terminal

    # Declaração de variáveis auxiliares e de retorno:
    opcao = ''
    tabela = ''
    dados = []
    informacao = ()
    principal = True  # Flag do looping principal

    # Looping da função
    while principal:
        limpar_terminal()
        # Menu da função:
        print('<::::::::::> CRIAR <::::::::::>')
        print('Em qual tabela você deseja inserir dados?')
        print('0 - Voltar')
        print('1 - Viajante')
        print('2 - Telefone')
        print('3 - Companhia')
        print('4 - Avião')
        print('5 - Passagem')
        print('6 - Rota')

        # Escolhe da tabela
        opcao = input('Digite o número da opção que deseja: ').strip()

        # Opção que volta para o menu principal:
        if opcao == '0':
            break

        # Inserção na tabela viajante:
        elif opcao == '1':
            tabela = 'viajante'

            # Looping de inserção de dados:
            while True:
                limpar_terminal()
                print('<::::::::::> VIAJANTE <::::::::::>')

                nome = input('Digite o nome do viajante: ').strip().lower()

                cpf = input('Digite o cpf do viajante: ').strip().lower()

                idade = input('Digite a idade do viajante: ').strip().lower()

                email = input('Digite o email do viajante: ').strip().lower()

                # Salvando uma copia das informações em dados e limpando informacao:
                informacao = (nome, cpf, idade, email)
                dados.append(informacao)
                informacao = ()

                # Dando ao usuário a opção de adicionar mais dados:
                opcao = input(
                    'Deseja inserir mais dados na tabela viajante (s/n): '
                ).strip().lower()
                if opcao == 's':
                    continue
                else:
                    principal = False
                    break

        # Inserção na tabela telefone:
        elif opcao == '2':
            tabela = 'telefone'

            # Looping de inserção de dados:
            while True:
                limpar_terminal()
                # Exibe a tabela viajante para permitir a correta relação entre viajante e telefone:
                print('<::::::::::> VIAJANTE <::::::::::>')
                exibir_tabela('viajante')

                print('<::::::::::> TELEFONE <::::::::::>')

                id_viajante = input(
                    'Digite o id do viajante dono do telefone: '
                ).strip().lower()

                telefone = input(
                    'Digite o número de telefone: ').strip().lower()

                # Salvando uma copia das informações em dados e limpando informacao:
                informacao = (id_viajante, telefone)
                dados.append(informacao)
                informacao = ()

                # Dando ao usuário a opção de adicionar mais dados:
                opcao = input(
                    'Deseja inserir mais dados na tabela viajante (s/n): '
                ).strip().lower()
                if opcao == 's':
                    continue
                else:
                    principal = False
                    break

        # Inserção na tabela companhia:
        elif opcao == '3':
            tabela = 'companhia'

            # Looping de inserção de dados:
            while True:
                limpar_terminal()
                print('<::::::::::> COMPANHIA <::::::::::>')

                nome = input(
                    'Digite o nome da companhia aérea: ').strip().lower()

                # Salvando uma copia das informações em dados e limpando informacao:
                informacao = (nome, )
                dados.append(informacao)
                informacao = ()

                # Dando ao usuário a opção de adicionar mais dados:
                opcao = input(
                    'Deseja adicionar mais dados na tabela companhia (s/n): '
                ).strip().lower()
                if opcao == 's':
                    continue
                else:
                    principal = False
                    break

        # Inserção na tabela aviao:
        elif opcao == '4':
            tabela = 'aviao'

            # Looping de inserção de dados:
            while True:
                limpar_terminal()
                # Exibe a tabela companhia para permitir a correta relação entre companhia e aviao:
                print('<::::::::::> COMPANHIA <::::::::::>')
                exibir_tabela('companhia')

                print('<::::::::::> AVIÃO <::::::::::>')

                id_companhia = input(
                    'Digite o id da companhia dona do avião: '
                ).strip().lower()

                nome = input('Digite o nome do avião: ').strip().lower()

                modelo = input('Digite o modelo do avião: ').strip().lower()

                ano_fabricacao = input(
                    'Digite o ano de fabricação do avião: ').strip().lower()

                numero_voos = input(
                    'Digite o número de voos do avião: ').strip().lower()

                numero_assentos = input(
                    'Digite o número de assentos: ').strip().lower()

                # Salvando uma copia das informações em dados e limpando informacao:
                informacao = (id_companhia, nome, modelo,
                              ano_fabricacao, numero_voos, numero_assentos)
                dados.append(informacao)
                informacao = ()

                # Dando ao usuário a opção de adicionar mais dados:
                opcao = input(
                    'Deseja adicionar mais dados na tabela avião (s/n): '
                ).strip().lower()
                if opcao == 's':
                    continue
                else:
                    principal = False
                    break

        # Inserção na tabela passagem:
        elif opcao == '5':
            tabela = 'passagem'

            # Looping de inserção de dados:
            while True:
                limpar_terminal()
                # Exibe a tabela viajante para a correta relação entre viajante e passagem:
                print('<::::::::::> VIAJANTE <::::::::::>')
                exibir_tabela('viajante')

                print('<::::::::::> PASSAGEM <::::::::::>')

                id_viajante = input(
                    'Digite o id do viajante: ').strip().lower()

                # Exibe a tabela aviao para a correta relação entre aviao e passagem:
                print('<::::::::::> AVIÃO <::::::::::>')
                exibir_tabela('aviao')

                id_aviao = input('Digite o id do avião: ').strip().lower()

                # Exibe a tabela rota para a correta relação entre rota e passagem:
                print('<::::::::::> ROTA <::::::::::>')
                exibir_tabela('rota')

                id_rota = input('Digite o id da rota: ').strip().lower()

                data_hora_partida = input(
                    'Digite a data e hora de partida (aaaa/mm/dd - hh:mm): '
                ).strip().lower()

                data_hora_chegada = input(
                    'Digite a data e hora de chegada (aaaa/mm/dd - hh:mm): '
                ).strip().lower()

                data_hora_volta = input(
                    'Digite a data e hora de volta (aaaa/mm/dd - hh:mm): '
                ).strip().lower()

                numero_paradas = input(
                    'Digite o número de paradas do voo: ').strip().lower()

                assentos_diponiveis = input(
                    'Digite o número de assentos disponíveis: '
                ).strip().lower()

                preco = input(
                    'Digite o preço da passagem (R$ 00000.00): '
                ).strip().lower()

                print('<::::::::::> FORMAS DE PAGAMENTO <::::::::::>')
                print('1 - Pix')
                print('2 - Dinheiro')
                print('3 - Cheque')
                print('4 - Cartão Crédito')
                print('5 - Cartão Débito')
                print('6 - Boleto')
                print('7 - Parcelamento')

                forma_pagamento = input(
                    'Digite o n° da forma de pagamento: ').strip().lower()

                # Salvando uma copia das informações em dados e limpando informacao:
                informacao = (id_viajante, id_aviao, id_rota,
                              data_hora_partida, data_hora_chegada,
                              data_hora_volta, numero_paradas,
                              assentos_diponiveis, preco, forma_pagamento)
                dados.append(informacao)
                informacao = ()

                # Dando ao usuário a opção de adicionar mais dados:
                opcao = input(
                    'Deseja adicionar mais dados na tabela passagem (s/n): '
                    ).strip().lower()
                if opcao == 's':
                    continue
                else:
                    principal = False
                    break

        # Inserção na tabela rota
        elif opcao == '6':
            tabela = 'rota'

            # Looping de inserção de dados:
            while True:
                limpar_terminal()
                print('<::::::::::> ROTA <::::::::::>')

                cidade_partida = input(
                    'Digite o nome da cidade de partida: ').strip().lower()

                cidade_chegada = input(
                    'Digite o nome da cidade de chegada: ').strip().lower()

                duracao = input(
                    'Digite a duração estimada do voo (00h 00m): '
                ).strip().lower()

                # Salvando ums copia das informações em dados e limpando informacao:
                informacao = (cidade_partida, cidade_chegada, duracao)
                dados.append(informacao)
                informacao = ()

                # Dando ao usuário a opção de adicionar mais dados:
                opcao = input(
                    'Deseja adicionar mais dados na tabela avião(s/n): '
                ).strip().lower()
                if opcao == 's':
                    continue
                else:
                    principal = False
                    break

        else:
            print('Opção inválida: digite apenas números!')
            input('Pressione qualquer tecla para continuar...')
            continue

    # retorno da função
    return tabela, dados
