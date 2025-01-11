# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Autor: Brendon João Campos Neves.
# Data: 09/12/2024.
# Módulo onde seram encapsuladas as funções desse pacote em uma classe para facilitar a importação:

# Importando as funções dos outros módulos:
from back_end.criar import criar_registro
from back_end.visualizar import visualizar_registro
from back_end.atualizar import atualizar_registro
from back_end.deletar import deletar_registro

# Criação da classe:
class Sistema:
    def __init__(self):
        pass
    
    def criar(self, tabela, dados):
        criar_registro(tabela, dados)
    
    def ler(self, tabela):
        visualizar_registro(tabela)
    
    def atualizar(self, tabela, dados):
        atualizar_registro(tabela, dados)
    
    def deletar(self, tabela, identificador):
        deletar_registro(tabela, identificador)