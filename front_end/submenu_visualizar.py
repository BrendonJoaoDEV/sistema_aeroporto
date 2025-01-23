# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Autor: Brendon João Campos Neves.
# Data: 10/01/2025.
# Módulo onde será definida a função que recebe e trata os dados da opção visualizar do menu principal.

def submenu_visualizar():
    """Submenu Visualizar
    """    
    
    # Importação de módulos:
    from front_end.exibir_tabela import exibir_tabela
    from front_end.limpar_terminal import limpar_terminal

    # Looping da função:
    while True:
        limpar_terminal()
        # Exbindo mnu da função
        print('<::::::::::> VISUALIZAR <::::::::::>')
        print('0 - Voltar para o menu principal')
        print('1 - Ver os dados de todos os viajantes')
        print('2 - Ver os telefones de todos os viajantes')
        print('3 - Ver os dados de todas as companhias')
        print('4 - Ver os dados de todos os aviões')
        print('5 - Ver os dados de todas as passagens')
        print('6 - Ver todas as rotas')
        print('7 - Ver os dados dos viajantes e seus telefones')
        print('8 - Ver todas as companhias e seus aviões')
        print('9 - Ver todas as passagens completas')

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
        
        elif opcao == '7':
            print('<::::::::::> VIAJANTE E TELEFONE <::::::::::>')
            exibir_tabela('viajante_telefone')
            input('Pressione qualquer tecla para continuar...')
            continue
        
        elif opcao == '8':
            print('<::::::::::> COMPANHIA E AVIÃO <::::::::::>')
            exibir_tabela('companhia_aviao')
            input('Pressione qualquer tecla para continuar...')
            continue
        
        elif opcao == '9':
            print('<::::::::::> PASSAGEM COMPLETA <::::::::::>')
            exibir_tabela('passagem_relacionados')
            input('Pressione qualquer tecla para continuar...')
            continue

        else:
            print('Opção inválida: digite apenas números!')
            input('Pressione qualquer tecla para continuar...')
            continue
