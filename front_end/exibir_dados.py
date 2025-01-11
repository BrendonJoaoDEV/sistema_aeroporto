# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Autor: Brendon João Campos Neves.
# Data: 08/01/2025.
# Módulo com função que faz uso da biblioteca prettytable para exibir
# dados na tela:

# Definição da função:
def exibir_dados(dados, fonte):
    """Exibir Dados

    Args:
        dados (tupla): variável com que armazana o valor de um cursor.fetch...
        fonte (object): obejto cursor do sqlite3.
    """
    # Importação da biblbioteca e da função:
    from prettytable import PrettyTable

    # Criando objeto PrettyTable:
    tabela = PrettyTable()

    # Obtendo os nomes dos campos:
    colunas = [descricao[0] for descricao in fonte.description]

    # Define os nomes da colunas:
    tabela.field_names = colunas

    # Adiciona as informações a tabela:
    for informacao in dados:
        tabela.add_row(informacao)

    print(tabela)
