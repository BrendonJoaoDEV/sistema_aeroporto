# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Brendon João Campos Neves.
# Data: 06/12/2024.
# Módulo onde será definida a função que cria registros no banco:

# Definição da função:
def criar_registro(tabela, dados):
    """Criar registro

    Args:
        tabela (string): nome da tabela que os dados devem ser inseridos.
        dados (list): lista de tuplas com os dados.

    Returns:
        string: mensagem dizendo se a operação funcionou ou falhou.
    """

    # Importação da biblioteca sqlite e os placeholders:
    import sqlite3
    from banco_dados.placeholders import inserts

    # Criação de uma conexão com o banco e um cursor para manipulação:
    conexao = sqlite3.connect('banco_dados/bancos_dados.db')
    cursor = conexao.cursor()

    # Verificão de qual tabela será usada para agir de acordo:
    if tabela == 'viajante':
        cursor.executemany(inserts['viajante'], dados)
        resposta = 'Inserção concluída'

    elif tabela == 'telefone':
        cursor.executemany(inserts['telefone'], dados)
        resposta = 'Inserção concluída'

    elif tabela == 'companhia':
        cursor.executemany(inserts['companhia'], dados)
        resposta = 'Inserção concluída'

    elif tabela == 'aviao':
        cursor.executemany(inserts['aviao'], dados)
        resposta = 'Inserção concluída'

    elif tabela == 'rota':
        cursor.executemany(inserts['rota'], dados)
        resposta = 'Inserção concluída'

    elif tabela == 'passagem':
        cursor.executemany(inserts['passagem'], dados)
        resposta = 'Inserção concluída'

    else:
        resposta = 'Falha na inserção: tabela não encontrada'

    # Salvando os dados e fechando a conexão:
    conexao.commit()
    conexao.close()

    # Retorno da função:
    return resposta
