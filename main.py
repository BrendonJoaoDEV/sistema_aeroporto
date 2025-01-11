# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 11/01/2025.
# Autor: Brendon João Campos Neves.
# Módulo principal do sistema que fará a junção dos pacotes:
# back_end, front_end e banco_dados para executar o sistema:

# Importação dos pacotes:
from front_end.classe_menu import Menu
from back_end.classe_sistema import Sistema
from banco_dados.criacao_tabelas import criar_banco

# Criando objetos para manipular a classe:
front_end = Menu()
back_end = Sistema()

# Criando banco de dados caso ele não exista:
criar_banco()

# Declaração de variáveis auxiliares:
tabela = ''
identificador = 0
dados = ()

# Looping pra manter o sistema até que seja o usuário queira sair:
while True:
    # Limpando o terminal ao iniciar ou voltar para o menu:
    front_end.limpar_terminal()

    # Exibindo as opções do menu:
    print('<::::::::::> HIPPOFRIFF AIRLINES <::::::::::>')
    print('0 - Sair do sistema')
    print('1 - Adicionar novos dados')
    print('2 - Atualizar dados existentes')
    print('3 - Visualizar dados existentes')
    print('4 - Deletar dados existentes')

    # Pedindo ao usuário para selecionar uma opção:
    opcao = input('Digite o número da opção que deseja executar: ')

    # Agindo de acordo com a opção escolhida:
    if opcao == '0':
        # Tela final do sistema:
        print('<' + ':'*70 + '>')
        print()
        print('Obrigado por usar nosso sitema ;)')
        print()
        print('<' + ':'*70 + '>')
        print()
        input('Pressione qualquer tecla para encerrar a sessão...')
        break

    elif opcao == '1':
        # Desempacotando os retornos da função submenu_criar:
        tabela, dados = front_end.submenu_criar()

        # Passando esses retornos para a função criar:
        back_end.criar(tabela, dados)

        # Mensagem de sucesso:
        print()
        print('Dados inseridos com sucesso!')
        input('Pressione qualquer tecla para continuar...')
        continue

    elif opcao == '2':
        # Desempacotando os retornos da função  submenu_atualizar:
        tabela, dados = front_end.submenu_atualizar()

        # Passando esses retornos para a função atualizar:
        back_end.atualizar(tabela, dados)

        # Mensagem de sucesso:
        print()
        print('Dados atualizados com sucesso!')
        input('Pressione qualquer tecla para continuar...')
        continue

    elif opcao == '3':
        # O submenu_visualizar já faz a sua integração com o back_end internamente:
        front_end.submenu_visualizar()
        continue

    elif opcao == '4':
        # Desempacotando os retornos da função submenu_deletar:
        tabela, identificador = front_end.submenu_deletar()

        # Passando esses retornos para a função deletar:
        back_end.deletar(tabela, identificador)

        # Mensagem de sucesso:
        print()
        print('dados deletados com sucesso!')
        input('Pressione qualquer tecla para continuar...')
        continue

    else:
        print('Opção inválida: por favor digite' +
              'apenas o número correspondente a uma opção!')
        input('Pressione qualquer tecla para continuar...')
        continue
