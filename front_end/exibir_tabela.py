# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Autor: Brendon João Campos Neves.
# Data: 11/12/2024.
# Módulo com função que faz uso da função vizualizar registro
# e a biblioteca prettytable para exibir tabelas:

# Definição da função:
def exibir_tabela(nome_tabela):
    """Exibir tabela

    Args:
        nome_tabela (string): nome da tabela para uso da função visualizar_resgistro.
    """

    # Importação da biblbioteca e da função:
    from prettytable import PrettyTable
    from back_end.visualizar import visualizar_registro

    # Pegando os dados apartir da função visualizar_registro:
    resultados, cursor = visualizar_registro(nome_tabela)

    # Criando objeto PrettyTable:
    tabela = PrettyTable()

    # Obtendo os nomes dos campos:
    colunas = [descricao[0] for descricao in cursor.description]

    # Define os nomes da colunas:
    tabela.field_names = colunas

    # Adiciona as informações a tabela:
    for informacao in resultados:
        tabela.add_row(informacao)

    print(tabela)
