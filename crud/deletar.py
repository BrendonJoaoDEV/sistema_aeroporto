# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Brendon João Campos Neves.
# Data: 06/12/2024.
# Módulo onde será definida a função que deleta registro no banco:

# Definição da tabela:
def deletar_registro(tabela, identificador):
    # Importação sqlite e dos placeholders:
    import sqlite3
    from banco_dados.placeholders import deletes

    # Criação de uma conexão e um cursor:
    conexao = sqlite3.connect('banco_dados/bancos_dados.db')
    cursor = conexao.cursor()

    # Deletando um ou mais dados:
    if tabela == 'viajante':
        cursor.executemany(deletes['viajante'], identificador)
        resposta = 'Exclusão concluída'

    elif tabela == 'telefone':
        cursor.executemany(deletes['telefone'], identificador)
        resposta = 'Exclusão concluída'

    elif tabela == 'companhia':
        cursor.executemany(deletes['companhia'], identificador)
        resposta = 'Exclusão concluída'

    elif tabela == 'aviao':
        cursor.executemany(deletes['aviao'], identificador)
        resposta = 'Exclusão concluída'

    elif tabela == 'rota':
        cursor.executemany(deletes['rota'], identificador)
        resposta = 'Exclusão concluída'

    elif tabela == 'passagem':
        cursor.executemany(deletes['passagem'], identificador)
        resposta = 'Exclusão concluída'

    else:
        resposta = 'Falha na exclusão: tabela não encontrada'

    # Salvando e fechando a conexão:
    conexao.commit()
    conexao.close()

    # Retorno da função:
    return resposta
