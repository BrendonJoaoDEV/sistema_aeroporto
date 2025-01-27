# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Autor: Brendon João Campos Neves.
# Data: 09/12/2024.
# Módulo onde será definida a função que atualiza registros existentes no banco:

# Definição da função:
def atualizar_registro(tabela, novo_registro):
    """Atualizar registro

    Args:
        tabela (string): nome da tabela que será alterada.
        identificador (int): um id que identifica unicamente cada registro.
        novo_registro (list): novos dados para o registro identificado.

    Returns:
        string: Mensagem dizendo se operação funcionou ou falhou.
    """

    # Imporção do sqlite e dos placeholders:
    import sqlite3
    from banco_dados.placeholders import updates

    # Criação de uma conexão e um cursor:
    conexao = sqlite3.connect("banco_dados/bancos_dados.db")
    cursor = conexao.cursor()

    # Encontrando a tabela e o registro para atualizar:
    if tabela == 'viajante':
        cursor.executemany(updates['viajante'], novo_registro)
        resposta = 'Atualização concluída'

    elif tabela == 'telefone':
        cursor.executemany(updates['telefone'], novo_registro)
        resposta = 'Atualização concluída'

    elif tabela == 'companhia':
        cursor.executemany(updates['companhia'], novo_registro)
        resposta = 'Atualização concluída'

    elif tabela == 'aviao':
        cursor.executemany(updates['aviao'], novo_registro)
        resposta = 'Atualização concluída'

    elif tabela == 'rota':
        cursor.executemany(updates['rota'], novo_registro)
        resposta = 'Atualização concluída'

    elif tabela == 'passagem':
        cursor.executemany(updates['passagem'], novo_registro)
        resposta = 'Atualização concluída'

    else:
        resposta = 'Falha na atualização: tabela não encontrada'

    # Salvando e fechando a conexão:
    conexao.commit()
    conexao.close()

    # Retorno da função:
    return resposta
