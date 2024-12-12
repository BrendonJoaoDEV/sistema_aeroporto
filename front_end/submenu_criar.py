# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Brendon João Campos Neves.
# Data: 11/12/2024.
# Módulo onde será definida a função que recebe e trata os dados da opção criar do menu principal.

# Definição da função:
def opcao_1():
    # Importação da função exibir_tabela:
    from front_end.exibir_tabela import exibir_tabela

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
        opcao = input('Digite o número da opção que deseja: ').strip()

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
                    break

        # Inserção na tabela telefone:
        elif opcao == '2':
            tabela = 'telefone'

            # Looping de inserção de dados:
            while True:
                # Exibe a tabela viajante para permitir a correta relação entre viajante e telefone:
                exibir_tabela('viajante')

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
                    break

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
            tabela = 'aviao'

            # Looping de inserção de dados:
            while True:
                # Exibe a tabela companhia para permitir a correta relação entre companhia e aviao:
                exibir_tabela('companhia')

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
                    break

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
