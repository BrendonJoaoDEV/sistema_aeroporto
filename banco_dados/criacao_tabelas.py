# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Autor: Brendon João Campos Neves.
# Data: 05/12/2024.
# Módulo onde são definidas todas as tabelas do banco de dados.

# Definição da função:
def criar_banco():
    # Importando a biblioteca:
    import sqlite3

    # Criando a conexão com o banco de dados:
    conexao = sqlite3.connect('banco_dados/bancos_dados.db')

    # Criando um cursor (objeto que executa comandos SQL):
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS viajante (
            id_viajante INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_viajante TEXT,
            cpf INTEGER,
            idade INTEGER,
            email TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS telefone (
            id_telefone INTEGER PRIMARY KEY AUTOINCREMENT,
            id_viajante INTEGER,
            telefone INTEGER,
            FOREIGN KEY (id_viajante) REFERENCES viajante(id_viajante) ON DELETE CASCADE
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS companhia (
            id_companhia INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_companhia TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS aviao (
            id_aviao INTEGER PRIMARY KEY AUTOINCREMENT,
            id_companhia INTEGER,
            nome_aviao TEXT,
            modelo_aviao TEXT,
            ano_fabricacao INTEGER,
            numero_voos INTEGER,
            numero_assentos INTEGER,
            FOREIGN KEY (id_companhia) REFERENCES companhia(id_companhia) ON DELETE CASCADE
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rota (
            id_rota INTEGER PRIMARY KEY AUTOINCREMENT,
            cidade_partida TEXT,
            cidade_chegada TEXT,
            duracao TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passagem (
            id_passagem INTEGER PRIMARY KEY AUTOINCREMENT,
            id_viajante INTEGER,
            id_aviao INTEGER,
            id_rota INTEGER,
            data_hora_partida TEXT,
            data_hora_chegada TEXT,
            data_hora_volta TEXT,
            numero_paradas INTEGER,
            assentos_disponiveis INTEGER,
            preco REAL,
            forma_pagamento TEXT,
            FOREIGN KEY (id_viajante) REFERENCES viajante(id_viajante),
            FOREIGN KEY (id_aviao) REFERENCES aviao(id_aviao),
            FOREIGN KEY (id_rota) REFERENCES rota(id_rota)
        );
    ''')

    # Salvando e fechando a conexão:
    conexao.commit()
    conexao.close()
