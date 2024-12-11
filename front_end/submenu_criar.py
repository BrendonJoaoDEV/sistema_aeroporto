# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Brendon João Campos Neves.
# Data: 010/12/2024.
# Módulo onde será definida a função com código referente a entrada de dados
# para a opção número 1 do menu principal.

# Definição da função:
def opcao_1():
    # Importação do PrettyTable e do sqlite:
    import sqlite3
    from prettytable import PrettyTable
    
    # Declaração de variáveis auxiliares e de retorno:
    tabela = ''
    dados = []
    informacao = ()

    # Looping da função
    while True:
        # Menu da função:
        print('Em qual tabela você deseja inserir dados?')
        print('0 - Voltar')
        print('1 - Viajante')
        print('2 - Telefone')
        print('3 - Companhia')
        print('4 - Avião')
        print('5 - Passagem')
        print('6 - Rota')

        # Escolhe da tabela
        opcao = input('Digite o númeroda opção que deseja: ').strip()

        # Opção que volta para o menu principal:
        if opcao == '0':
            break

        # Inserção na tabela viajante:
        elif opcao == '1':
            tabela = 'viajante'

            # Looping de inserção de dados:
            while True:
                nome = input('Digite o nome do viajante: ').strip().lower()

                cpf = input('Digite o cpf do viajante: ').strip().lower()
                # Validando e removendo . e - do cpf:
                if '.' in cpf or '-' in cpf:
                    cpf = cpf.replace('.', '') and cpf.replace('-', '')
                    if cpf.isdigit():
                        cpf = int(cpf)
                    else:
                        print('cpf inválido, digite apenas números')
                        continue

                idade = input('Digite a idade do viajante: ').strip().lower()
                if idade.isdigit():
                    idade = int(idade)
                else:
                    print('Idade inválida, digite apenas números')
                    continue

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
                    break

        # Inserção na tabela telefone:
        elif opcao == '2':
            pass

        # Inserção na tabela companhia:
        elif opcao == '3':
            tabela = 'companhia'

            # Looping de inserção de dados:
            while True:
                nome = input(
                    'Digite o nome da companhia aérea: ').strip().lower()

                # Salvando uma copia das informações em dados e limpando informacao:
                informacao = (nome)
                dados.append(informacao)
                informacao = ()

                # Dando ao usuário a opção de adicionar mais dados:
                opcao = input(
                    'Deseja adicionar mais dados na tabela companhia (s/n): '
                    ).strip().lower()
                if opcao == 's':
                    continue
                else:
                    break

        # Inserção na tabela aviao:
        elif opcao == '4':
            pass

        # Inserção na tabela passagem:
        elif opcao == '5':
            pass
        
        # Inserção na tabela rota
        elif opcao == '6':
            pass

        else:
            pass

    # retorno da função
    return tabela, dados
