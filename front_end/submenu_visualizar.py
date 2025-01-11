# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Brendon João Campos Neves.
# Data: 10/01/2025.
# Módulo onde será definida a função que recebe e trata os dados da opção visualizar do menu principal.

def submenu_visualizar():
    # Importação de módulos:
    from front_end.exibir_tabela import exibir_tabela
    from front_end.limpar_terminal import limpar_terminal

    # Looping da função:
    while True:
        limpar_terminal()
        # Exbindo mnu da função
        print('<::::::::::> VISUALIZAR <::::::::::>')
        print('Qual dessas tabelas vocÊ deseja visualizar?')
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
            print('<::::::::::> VIAJANTE <::::::::::>')
            exibir_tabela('viajante')
            input('Pressione qualquer tecla para continuar...')
            continue

        elif opcao == '2':
            print('<::::::::::> TELEFONE <::::::::::>')
            exibir_tabela('telefone')
            input('Pressione qualquer tecla para continuar...')
            continue

        elif opcao == '3':
            print('<::::::::::> COMPANHIA <::::::::::>')
            exibir_tabela('companhia')
            input('Pressione qualquer tecla para continuar...')
            continue

        elif opcao == '4':
            print('<::::::::::> AVIÃO <::::::::::>')
            exibir_tabela('aviao')
            input('Pressione qualquer tecla para continuar....')
            continue

        elif opcao == '5':
            print('<::::::::::> PASSAGEM <::::::::::>')
            exibir_tabela('passagem')
            input('Pressione qualquer tecla para continuar...')
            continue

        elif opcao == '6':
            print('<::::::::::> ROTA <::::::::::>')
            exibir_tabela('rota')
            input('Pressione qualquer tecla para continuar...')
            continue

        else:
            print('Opção inválida: digite apenas números!')
            input('Pressione qualquer tecla para continuar...')
            continue
