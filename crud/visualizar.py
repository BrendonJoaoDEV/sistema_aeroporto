# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Brendon João Campos Neves.
# Data: 09/12/2024.
# Módulo onde será definida a função que imprime registro no banco:

# Definição da função:
def visualizar_registro(campos, tabelas, condicao):
    # Importação do sqlite e do prettytable:
    import sqlite3

    # Criação de uma conexão e um cursor:
    conexao = sqlite3.connect('banco_dados/bancos_dados.db')
    cursor = conexao.cursor()

    # Analisando como a query deve ser formada:
    if len(tabelas) == 1:
        cursor.execute(f'''SELECT {campos} FROM {tabelas} WHERE {condicao}''')
        resultado = cursor.fetchall()

    elif len(tabelas) == 2:
        # Lógica para substituir o nome das tabelas e chaves
        # Para formar querys com quaisqueres tabelas que forem passadas.
        cursor.execute(f'''SELECT {campos} FROM {tabelas[0]}
                       INNER JOIN {tabelas[0]}.id_{tabelas[1]} = 
                       {tabelas[1]}.id_{tabelas[1]}
                       WHERE {condicao}''')
        resultado = cursor.fetchall()

    else:
        resultado = 'Operação não planejada :/'

    # Retorno da função:
    return resultado
