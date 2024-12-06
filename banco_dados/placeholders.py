# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Brendon João Campos Neves.
# Data: 06/12/2024.
# Módulo onde seram definidos placeholders padrões para cada tabela,
# isso servirá para evitar invasões SQL injection.

placeholders = {
    'viajante' : '''INSERT INTO viajante 
                    (id_viajante, nome_viajante, cpf, idade, email)
                    VALUES (?, ?, ?, ?, ?)''',

    'telefone' : '''INSERT INTO telefone
                    (id_telefone, id_viajante, telefone)
                    VALUES (?, ?, ?)''',

    'companhia' : '''INSERT INTO companhia
                    (id_companhia, nome_companhia)
                    VALUES (?, ?)''',

    'aviao' : '''INSERT INTO aviao
                (id_aviao, id_companhia, nome_aviao, modelo_aviao, 
                ano_fabricacao, numero_voos, numero_assentos)
                VALUES (?, ?, ?, ?, ?, ?, ?)''',

    'rota' : '''INSERT INTO rota
                (id_rota, cidade_partida, cidade_chegada, duracao)
                VALUES (?, ?, ?, ?)''',

    'passagem' : '''INSERT INTO passagem
                    (id_passagem, id_viajante, id_aviao, id_rota, 
                    data_hora_partida, data_hora_chegada, data_hora_volta, 
                    numero_paradas, assentos_disponiveis, preco, 
                    forma_pagamento)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
}