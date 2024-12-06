# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Brendon João Campos Neves.
# Data: 06/12/2024.
# Módulo onde será definida a função que cria registros no banco:

# Definição da função:
def criar_registro(tabela, dados):
    # Importção da biblioteca sqlite e os placeholders:
    import sqlite3
    from banco_dados.placeholders import placeholders

    # Criação de uma conexão com o banco e um cursor para manipulação:
    conexao = sqlite3.connect("banco_dados/bancos_dados.db")
    cursor = conexao.cursor()

    # Verificão de qual tabela será usada para agir de acordo:
    if tabela == 'viajante':
        cursor.executemany(placeholders['viajante'], dados)
        resposta = 'Inserção concluída'
    elif tabela == 'telefone':
        cursor.executemany(placeholders['telefone'], dados)
        resposta = 'Inserção concluída'
    elif tabela == 'companhia':
        cursor.executemany(placeholders['companhia'], dados)
        resposta = 'Inserção concluída'
    elif tabela == 'aviao':
        cursor.executemany(placeholders['aviao'], dados)
        resposta = 'Inserção concluída'
    elif tabela == 'rota':
        cursor.executemany(placeholders['rota'], dados)
        resposta = 'Inserção concluída'
    elif tabela == 'passagem':
        cursor.executemany(placeholders['passagem'], dados)
        resposta = 'Inserção concluída'
    else:
        resposta = 'Falha na inserção: tabela não encontrada'

    # Salvando os dados e fechando a conexão:
    conexao.commit()
    conexao.close()

    # Retorno da função:
    return resposta
