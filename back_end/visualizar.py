# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Autor: Brendon João Campos Neves.
# Data: 09/12/2024.
# Módulo onde será definida a função que imprime registro no banco:

# Definição da função:
def visualizar_registro(tabela):
    """visualizar registro

    Args:
        campos (string): string com os campos separados por vírgulas.
        tabelas (list): lista com strings dos nomes das tabelas que deseja ver.
        condicao (string): condição para que os dados sejam retornados ou não.

    Returns:
        resultado(list or string): lista contendo os dados que a query encontrou ou mensagem de erro.
        cursor(onject): objeto que pode ser usado para exibição de tabelas prettytable.
    """

    # Importação do sqlite e do prettytable:
    import sqlite3
    from banco_dados.placeholders import selects

    # Criação de uma conexão e um cursor:
    conexao = sqlite3.connect('banco_dados/bancos_dados.db')
    cursor = conexao.cursor()

    # Analisando como a query deve ser formada:
    if tabela == 'viajante':
        cursor.execute(selects['viajante'])
        resultado = cursor.fetchall()
    
    elif tabela == 'telefone':
        cursor.execute(selects['telefone'])
        resultado = cursor.fetchall()
        
    elif tabela == 'companhia':
        cursor.execute(selects['companhia'])
        resultado = cursor.fetchall()
        
    elif tabela == 'aviao':
        cursor.execute(selects['aviao'])
        resultado = cursor.fetchall()
    elif tabela == 'rota':
        cursor.execute(selects['rota'])
        resultado = cursor.fetchall()
        
    elif tabela == 'passagem':
        cursor.execute(selects['passagem'])
        resultado = cursor.fetchall()
        
    else:
        resultado = 'Falha na visualização: tabela não encontrada'

    # Retorno da função:
    return resultado, cursor
