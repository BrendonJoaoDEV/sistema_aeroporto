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
                    id_viajante AS "ID",
                    nome_viajante AS "Nome",
                    cpf AS "CPF",
                    idade AS "Idade",
                    email AS "Email"
                    FROM viajante''',

    'telefone': '''SELECT 
                    id_telefone AS "ID",
                    id_viajante AS "ID do Viajante",
                    telefone AS "Telefone"
                    FROM telefone''',

    'companhia': '''SELECT
                    id_companhia AS "ID",
                    nome_companhia AS "Nome da Companhia"
                    FROM companhia''',

    'aviao': '''SELECT
                id_aviao AS "ID",
                id_companhia AS "ID da Companhia",
                nome_aviao AS "Nome do Avião",
                modelo_aviao AS "Modelo",
                ano_fabricacao AS "Ano de Fabricação",
                numero_voos AS "Número de Voos",
                numero_assentos AS "Número de Assentos"
                FROM aviao''',

    'rota': '''SELECT
                id_rota AS "ID",
                cidade_partida AS "Cidade de Partida",
                cidade_chegada AS "Cidade de Chegada",
                duracao AS "Duração"
                FROM rota''',

    'passagem': '''SELECT
                    id_passagem AS "ID",
                    id_viajante AS "ID do Viajante",
                    id_aviao AS "ID do Avião",
                    id_rota AS "ID da Rota",
                    data_hora_partida AS "Data e Hora de Partida",
                    data_hora_chegada AS "Data e Hora de Chegada",
                    data_hora_volta AS "Data e Hora de Volta",
                    numero_paradas AS "Número de Paradas",
                    assentos_disponiveis AS "Assentos Disponíveis",
                    preco AS "Preço",
                    forma_pagamento AS "Forma de Pagamento"
                    FROM passagem''',

    'viajante_telefone': '''SELECT 
                                viajante.nome_viajante AS "Nome",
                                viajante.cpf AS "CPF",
                                viajante.idade AS "Idade",
                                viajante.email AS "Email",
                                telefone.telefone AS "Telefone"
                            FROM viajante
                            JOIN telefone ON viajante.id_viajante = telefone.id_viajante
                                ''',

    'companhia_aviao': '''SELECT
                                companhia.nome_companhia AS "Nome Companhia",
                                aviao.nome_aviao AS "Nome do Avião",
                                aviao.modelo_aviao AS "Modelo do Avião",
                                aviao.ano_fabricacao AS "Ano de Fabricação",
                                aviao.numero_voos AS "Número de Voos",
                                aviao.numero_assentos AS "Número de Assentos"
                            FROM companhia
                            JOIN aviao ON companhia.id_companhia = aviao.id_companhia
                            ''',

    'passagem_relacionados': '''SELECT
                                    viajante.nome_viajante AS "Nome do Viajante",
                                    viajante.cpf AS "CPF",
                                    aviao.nome_aviao AS "Nome do Avião",
                                    aviao.modelo_aviao AS "Modelo do Avião",
                                    rota.cidade_partida AS "Cidade de Partida",
                                    passagem.data_hora_partida AS "Data e Hora de Partida",
                                    rota.cidade_chegada AS "Cidade de Chegada",
                                    passagem.data_hora_chegada AS "Data e Hora de Chegada",
                                    rota.duracao AS "Duração",
                                    passagem.data_hora_volta AS "Data e hora de Retorno",
                                    passagem.preco AS "Preço da Passagem",
                                    passagem.forma_pagamento AS "Forma de Pagamento"
                                FROM passagem
                                JOIN viajante ON viajante.id_viajante = passagem.id_viajante
                                JOIN aviao ON aviao.id_aviao = passagem.id_aviao
                                JOIN rota ON rota.id_rota = passagem.id_rota
                                '''
}
