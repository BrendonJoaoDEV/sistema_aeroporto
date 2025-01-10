# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Brendon João Campos Neves.
# Data: 08/01/2025.
# Módulo com função que faz uso da biblioteca os para limpar o terminal:

# Definição da função:
def limpar_terminal():
    """Limpar Terminal
    """

    # Importação da biblioteca os:
    import os

    # Limpando o terminal
    os.system('cls' if os.name == 'nt' else 'clear')
