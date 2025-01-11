# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Autor: Brendon João Campos Neves.
# Data: 10/01/2025.
# Módulo onde será definida a função que recebe e trata os dados da opção deletar do menu principal.

def submenu_deletar():
    """Submenu Deletar

    Returns:
        string: nome da tabela para uso da função back_end.deletar.
        int: identificador para uso da função back_end.deletar.
    """    
    
    # Importação de módulos:
    from front_end.exibir_tabela import exibir_tabela
    from front_end.limpar_terminal import limpar_terminal

    # Declaração de variáveis de retorno e auxiliares:
    opcao = ''
    tabela = ''
    identificador = ''
    principal = True  # Flag do looping principal.

    # Looping da função:
    while principal:
        limpar_terminal()
        # Menu da função:
        print('<::::::::::> DELETAR <::::::::::>')
        print('De qual tabela você deseja deletar dados?')
        print('0 - Voltar')
        print('1 - Viajante')
        print('2 - Telefone')
        print('3 - Companhia')
        print('4 - Avião')
        print('5 - Passagem')
        print('6 - Rota')

        opcao = input('Digite o número da opção desejada: ').strip()

        if opcao == '0':
            break

        elif opcao == '1':
            tabela = 'viajante'

            while True:
                # Exibindo a tabela viajante:
                print('<::::::::::> VIAJANTE <::::::::::>')
                exibir_tabela('viajante')

                # Pedindo ao usuário para selecionar o viajante a ser deletado:
                identificador = input(
                    'Digite o id do viajante que deseja deletar: '
                    ).strip().lower()

                # Dando ao usuário a opção de apagar outro viajante:
                opcao = input(
                    'Deseja deletar outro viajante (s/n): '
                    ).strip().lower()

                if opcao == 's':
                    continue
                else:
                    principal = False
                    break

        elif opcao == '2':
            tabela = 'telefone'

            while True:
                # Exibindo a tabela telefone:
                print('<::::::::::> TELEFONE <::::::::::>')
                exibir_tabela('telefone')

                # Pedindo ao usuário para selecionar o telefone a ser deletado:
                identificador = input(
                    'Digite o id do telefone que deseja deletar: '
                    ).strip().lower()

                # Dando ao usuário a opção de apagar outro telefone:
                opcao = input(
                    'Deseja deletar outro telefone (s/n): '
                    ).strip().lower()

                if opcao == 's':
                    continue
                else:
                    principal = False
                    break

        elif opcao == '3':
            tabela = 'Companhia'

            while True:
                # Exibindo a tabela companhia:
                print('<::::::::::> COMPANHIA <::::::::::>')
                exibir_tabela('companhia')

                # Pedindo ao usuário para selecionar a companhia a ser deletada:
                identificador = input(
                    'Digite o id da companhia que deseja deletar: '
                    ).strip().lower()

                # Dando ao usuário a opção de apagar outra companhia:
                opcao = input(
                    'Deseja deletar outra companhia (s/n): '
                    ).strip().lower()

                if opcao == 's':
                    continue
                else:
                    principal = False
                    break

        elif opcao == '4':
            tabela = 'aviao'

            while True:
                # Exibindo a tabela aviao:
                print('<::::::::::> AVIÃO <::::::::::>')
                exibir_tabela('aviao')

                # Pedindo ao usuário para selecionar o avião a ser deletado:
                identificador = input(
                    'Digite o id do avião  que deseja deletar: '
                    ).strip().lower()

                # Dando ao usuário a opção de apagar outro avião:
                opcao = input(
                    'Deseja deletar outro avião (s/n): '
                    ).strip().lower()

                if opcao == 's':
                    continue
                else:
                    principal = False
                    break

        elif opcao == '5':
            tabela = 'passagem'

            while True:
                # Exibindo a tabela passagem:
                print('<::::::::::> PASSAGEM <::::::::::>')
                exibir_tabela('passagem')

                # Pedindo ao usuário para selecionar a passagem a ser deletada:
                identificador = input(
                    'Digite o id da passagem que deseja deletar: '
                    ).strip().lower()

                # Dando ao usuário a opção de apagar outra passagem:
                opcao = input(
                    'Deseja deletar outra passagem (s/n): '
                ).strip().lower()

                if opcao == 's':
                    continue
                else:
                    principal = False
                    break

        elif opcao == '6':
            tabela = 'rota'

            while True:
                # Exibindo a tabela rota:
                print('<::::::::::> ROTA <::::::::::>')
                exibir_tabela('rota')

                # Pedindo ao usuário para selecionar a rota a ser deletada:
                identificador = input(
                    'Digite o id da rota que deseja deletar: '
                    ).strip().lower()

                # Dando ao usuário a opção de apagar outra rota:
                opcao = input(
                    'Deseja deletar outra rota (s/n): '
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

    return tabela, identificador
