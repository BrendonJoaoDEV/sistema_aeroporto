# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Autor: Brendon João Campos Neves.
# Data: 10/01/2025.
# Módulo onde será definida a função que recebe e trata os dados da opção atualizar do menu principal.

def submenu_atualizar():
    """Submenu Atualizar

    Returns:
        string: nome da tabela para uso da função back_end.atualizar.
        int: identificador dos dados para uso da função back_end.atualizar.
        tupla: tupla com os novos dados para uso da função back_end.atualizar.
    """    
    
    # Importação de módulos:
    from front_end.exibir_tabela import exibir_tabela
    from front_end.limpar_terminal import limpar_terminal

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
        print('0 - Voltar para o menu principal')
        print('1 - Modificar dados de um viajante')
        print('2 - Modificar telefone de um viajante')
        print('3 - Modificar dados de uma companhia')
        print('4 - Modificar dados de um avião')
        print('5 - Modificar dados de uma passagem')
        print('6 - Modificar uma rota')

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

                # Pedindo os novos dados:
                nome = input('Digite o novo nome: ').strip().lower()

                cpf = input('Digite o novo cpf: ').strip().lower()

                idade = input('Digite a nova idade: ').strip().lower()

                email = input('Digite o novo email: ').strip().lower()

                # Salvando os novos dados
                informacao = (nome, cpf, idade, email, identificador)
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
                
                # Pedindo os novos dados:
                exibir_tabela('viajante')
                id_viajante = input('Digite o novo id do viajante: '
                                    ).strip().lower()

                telefone = input('Digite o novo telefone: ').strip().lower()

                # Salvando os novos dados:
                informacao = (id_viajante, telefone, identificador)
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

                # Pedindo os novos dados:
                nome = input('Digite o novo nome da companhia: ').strip().lower()

                # Salvando os novos dados:
                informacao = (nome, identificador)
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

                # Pedindo os novos dados:
                exibir_tabela('companhia')
                id_companhia = input('Digite a nova companhia: '
                                     ).strip().lower()

                nome = input('Digite o novo nome do avião: ').strip().lower()

                modelo = input('Digite o novo modelo do avião: '
                               ).strip().lower()

                fabricacao = input(
                    'Digite o novo ano de fabricação do avião: '
                    ).strip().lower()

                voos = input('Digite o novo número de voos do avião: '
                             ).strip().lower()

                assentos = input('Digite o novo número de assentos do avião: '
                                 ).strip().lower()

                # Salvando os novos dados:
                informacao = (id_companhia, nome, modelo,
                                fabricacao, voos, assentos,
                                identificador)
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

        elif opcao == '5':
            tabela == 'passagem'

            # Looping de alteração:
            while True:
                limpar_terminal()
                # Exibindo a tabela passagem e pedindo ao usuário para selecionar uma passagem:
                print('<::::::::::> PASSAGEM <::::::::::>')
                exibir_tabela('passagem')
                
                identificador = input(
                    'Qual o id da passagem que deseja alterar? '
                    ).strip().lower()
                
                # Pedindo os novos dados:
                exibir_tabela('viajante')
                id_viajante = input('Digite o id do novo viajante: '
                                    ).strip().lower()
                
                exibir_tabela('aviao')
                id_aviao = input(
                    'Digite o id do novo avião: ').strip().lower()
                
                exibir_tabela('rota')
                id_rota = input('Digite o id da nova rota: ').strip().lower()
                
                data_hora_partida = input(
                    'Digite a nova data e hora de partida ' + 
                    '(aaaa/mm/dd - hh/mm): ').strip().lower()
                
                data_hora_chegada = input(
                    'Digite a nova data e hora de chegada ' +
                    '(aaaa/mm/dd - hh/mm): ').strip().lower()
                
                data_hora_volta = input(
                    'Digite a nova data e hora de volta ' +
                    '(aaaa/mm/dd - hh/mm): ').strip().lower()
                
                paradas = input('Digite o novo número de paradas: '
                                ).strip().lower()
                
                assentos = input(
                    'Digite o novo número de assentos disponíveis: '
                    ).strip().lower()
                
                preco = input(
                    'Digite o novo preço (R$ 00000.00): ').strip().lower()
                
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

                # Salvando os novos dados:
                informacao = (id_viajante, id_aviao, id_rota,
                                data_hora_partida, data_hora_chegada,
                                data_hora_volta, paradas, assentos,
                                preco, forma_pagamento, identificador)
                novos_dados.append(informacao)
                informacao = ()
                
                # Dando ao usuário a opção de alterar outra passagem:
                opcao = input('Deseja alterar outra passagem (s/n): '
                                ).strip().lower()
                if opcao == 's':
                    continue
                else:
                    principal = False
                    break
                    
        elif opcao == '6':
            tabela = 'rota'

            # Looping de alteração:
            while True:
                limpar_terminal()
                # Exibindo a tabela rota e pedindo ao usuário para selecionar uma rota:
                print('<::::::::::> ROTA <::::::::::>')
                exibir_tabela('rota')
                
                identificador = input('Qual o id da rota que deseja alterar? '
                                      ).strip().lower()
                
                # Pedindo os novos dados:
                cidade_partida = input('Digite a nova cidade de partida: '
                                       ).strip().lower()
            
                cidade_chegada = input('Digite a nova cidade de chegada: '
                                       ).strip().lower()
                
                duracao = input('Digite a nova duração da rota: '
                                ).strip().lower()
                
                # Salvando os novos dados:
                informacao = (cidade_partida, cidade_chegada,
                              duracao, identificador)
                novos_dados.append(informacao)
                informacao = ()
                
                # Dando ao usuário a opção de alterar outra rota:
                opcao = input('Deseja atualizar outra rota (s/n): '
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

    # Retorno da função:
    return tabela, novos_dados
