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
    
    def criar(self):
        return criar_registro()
    
    def ler(self):
        return visualizar_registro()
    
    def atualizar(self):
        return atualizar_registro()
    
    def deletar(self):
        return deletar_registro()