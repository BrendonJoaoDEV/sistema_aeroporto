# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Brendon João Campos Neves.
# Data: 23/12/2024.
# Módulo onde será definida a função que recebe e trata os dados da opção atualizar do menu principal.

def submenu_2():
    # Importação da função exibir tabela:
    from front_end.exibir_tabela import exibir_tabela
    
    # Declaração de variáveis auxiliares e de retorno:
    opcao = ''
    tabela = ''
    identificador = ''
    novos_dados = ''
    
    # Looping da função:
    while True:
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
                print('<::::::::::> VIAJANTE <::::::::::>')
                exibir_tabela('viajante')
                
                identificador = input('Qual o id do viajante que deseja adicionar? ').strip().lower()
        elif opcao == '2':
            pass
        elif opcao == '3':
            pass
        elif opcao == '4':
            pass
        elif opcao == '5':
            pass
        elif opcao == '6':
            pass
        else:
            pass