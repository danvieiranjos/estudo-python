"""
Exemplo de tratamento de exceções (Try/Except).
Demonstra como capturar erros específicos e genéricos.
"""

lista = [1, 20]

try:
    divisao = 10 / 2
    numero = lista[1]  # Acessando índice existente
    print(f"Resultado da divisão: {divisao}")
except ZeroDivisionError:
    print("Erro: Não é possível realizar uma divisão por zero.")
except IndexError:
    print("Erro: O índice acessado não existe na lista.")
except BaseException as ex:
    print(f"Erro inesperado: {ex}")