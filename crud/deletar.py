# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Brendon João Campos Neves.
# Data: 06/12/2024.
# Módulo onde será definida a função que deleta registro no banco:

# Definição da tabela:
def deletar_registro(tabela, identificador):
    # Importação sqlite:
    import sqlite3

    # Criação de uma conexão e um cursor:
    conexao = sqlite3.connect("banco_dados/bancos_dados.db")
    cursor = conexao.cursor()

    # Deletando um ou mais dados:
    if tabela == 'viajante':
        cursor.executemany(
            '''DELETE FROM viajante WHERE id_viajante = ?''', identificador)
        resposta = 'Exclusão concluída'
    elif tabela == 'telefone':
        cursor.executemany(
            '''DELETE FROM telefone WHERE id_telefone = ?''', identificador)
        resposta = 'Exclusão concluída'
    elif tabela == 'companhia':
        cursor.executemany(
            '''DELETE FROM companhia WHERE id_companhia = ?''', identificador)
        resposta = 'Exclusão concluída'
    elif tabela == 'aviao':
        cursor.executemany(
            '''DELETE FROM aviao WHERE id_aviao = ?''', identificador)
        resposta = 'Exclusão concluída'
    elif tabela == 'rota':
        cursor.executemany(
            '''DELETE FROM rota WHERE id_rota = ?''', identificador)
        resposta = 'Exclusão concluída'
    elif tabela == 'passagem':
        cursor.executemany(
            '''DELETE FROM passagem WHERE id_passagem = ?''', identificador)
        resposta = 'Exclusão concluída'
    else:
        resposta = 'Falha na exclusão: tabela não encontrada'

    # Salvando e fechando a conexão:
    conexao.commit()
    conexao.close()

    # Retorno da função:
    return resposta
