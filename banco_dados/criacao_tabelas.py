# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Brendon João Campos Neves.
# Data: 05/12/2024.
# Módulo onde são definidas todas as tabelas do banco de dados.

# Importando a biblioteca:
import sqlite3

# Criando a conexão com o banco de dados:
conexao = sqlite3.connect("C:/Repositórios Brendon/Sistema_aeroporto/banco_dados/bancos_dados.db")

# Criando um cursor (objeto que executa comandos SQL):
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS viajante (
        id_viajante INTEGER,
        nome_viajante TEXT,
        cpf INTEGER,
        idade INTEGER,
        email TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS telefone (
        id_telefone INTEGER,
        id_viajante INTEGER,
        telefone INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS companhia (
        id_companhia INTEGER,
        nome_companhia TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS aviao (
        id_aviao INTEGER,
        id_companhia INTEGER,
        nome_aviao TEXT,
        modelo_aviao TEXT,
        ano_fabricacao INTEGER,
        numero_voos INTEGER,
        numero_assentos INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS rota (
        id_rota INTEGER,
        cidade_partida TEXT,
        cidade_chegada TEXT,
        duracao TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS passagem (
        id_passagem INTEGER,
        id_viajante INTEGER,
        id_aviao INTEGER,
        id_rota INTEGER,
        data_hora_partida TEXT,
        data_hora_chegada TEXT,
        data_hora_volta TEXT,
        numero_paradas INTEGER,
        assentos_diponiveis INTEGER,
        preco REAL,
        forma_pagamento TEXT
    )
''')