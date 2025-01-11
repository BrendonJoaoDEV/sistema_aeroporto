# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Autor: Brendon João Campos Neves.
# Data: 06/12/2024.
# Módulo onde seram definidos placeholders padrões para cada tabela,
# isso servirá para evitar invasões SQL injection, além de permitir
# uma melhor separação entre os códigos em Python e em SQL.

inserts = {
    'viajante': '''INSERT INTO viajante 
                    (nome_viajante, cpf, idade, email)
                    VALUES (?, ?, ?, ?)''',

    'telefone': '''INSERT INTO telefone
                    (id_viajante, telefone)
                    VALUES (?, ?)''',

    'companhia': '''INSERT INTO companhia
                    (nome_companhia)
                    VALUES (?)''',

    'aviao': '''INSERT INTO aviao
                (id_companhia, nome_aviao, modelo_aviao, 
                ano_fabricacao, numero_voos, numero_assentos)
                VALUES (?, ?, ?, ?, ?, ?)''',

    'rota': '''INSERT INTO rota
                (cidade_partida, cidade_chegada, duracao)
                VALUES (?, ?, ?)''',

    'passagem': '''INSERT INTO passagem
                    (id_viajante, id_aviao, id_rota, 
                    data_hora_partida, data_hora_chegada, data_hora_volta, 
                    numero_paradas, assentos_disponiveis, preco, 
                    forma_pagamento)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
}

deletes = {
    'viajante': '''DELETE FROM viajante WHERE id_viajante = ?''',

    'telefone': '''DELETE FROM telefone WHERE id_telefone = ?''',

    'companhia': '''DELETE FROM companhia WHERE id_companhia = ?''',

    'aviao': '''DELETE FROM aviao WHERE id_aviao = ?''',

    'rota': '''DELETE FROM rota WHERE id_rota = ?''',

    'passagem': '''DELETE FROM passagem WHERE id_passagem = ?'''
}

updates = {
    'viajante': '''UPDATE viajante SET nome_viajante = ?, cpf = ?,
                    idade = ?, email = ? WHERE id_viajante = ?''',

    'telefone': '''UPDATE telefone SET id_viajante = ?, telefone = ?
                    WHERE id_telefone = ?''',

    'companhia': '''UPDATE companhia SET nome_companhia = ? 
                    WHERE id_companhia = ?''',

    'aviao': '''UPDATE aviao SET id_companhia = ?, nome_aviao = ?, 
                modelo_aviao = ?, ano_fabricacao = ?, numero_voos = ?,
                numero_assentos = ? WHERE id_aviao = ?''',

    'rota': '''UPDATE rota SET cidade_partida = ?, cidade_chegada = ?,
                duracao = ? WHERE id_rota = ?''',

    'passagem': '''UPDATE passagem SET id_viajante = ?, id_aviao = ?,
                    id_rota = ?, data_hora_partida = ?, data_hora_chegada = ?,
                    data_hora_volta = ?, numero_paradas = ?,
                    assentos_disponiveis = ?, preco = ?, forma_pagamento = ?
                    WHERE id_passagem = ?'''
}

selects = {
    'viajante': '''SELECT 
                    id_viajante AS "id",
                    nome_viajante AS "nome",
                    cpf AS "cpf",
                    idade,
                    email
                    FROM viajante''',

    'telefone': '''SELECT 
                    id_telefone AS "id",
                    id_viajante AS "id viajante",
                    telefone
                    FROM telefone''',

    'companhia': '''SELECT
                    id_companhia AS "id",
                    nome_companhia AS "nome"
                    FROM companhia''',

    'aviao': '''SELECT
                id_aviao AS "id",
                id_companhia AS "id companhia",
                nome_aviao AS "nome",
                modelo_aviao AS "modelo",
                ano_fabricacao AS "ano de fabricação",
                numero_voos AS "número de voos",
                numero_assentos AS "número de assentos"
                FROM aviao''',

    'rota': '''SELECT
                id_rota AS "id",
                cidade_partida AS "cidade de partida",
                cidade_chegada AS "cidade de chegada",
                duracao AS "duração"
                FROM rota''',

    'passagem': '''SELECT
                    id_passagem AS "id",
                    id_viajante AS "id do viajante",
                    id_aviao AS "id do avião",
                    id_rota AS "id da rota",
                    data_hora_partida AS "data e hora de partida",
                    data_hora_chegada AS "data e hora de chegada",
                    data_hora_volta AS "dara e hora de volta",
                    numero_paradas AS "número de paradas",
                    assentos_disponiveis AS "assentos disponíveis"
                    preco AS "preço"
                    forma_pagamento AS "forma de pagamento"
                    FROM passagem'''
}
