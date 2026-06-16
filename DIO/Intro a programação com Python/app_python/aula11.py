
lista = [1, 20]
try:
    divisao = 10 / 0
    numero = lista[1]
    x = 1
# except ZeroDivisionError:
#     print("Não é possível realizar uma divisão por 0")
# except IndexError:
#     print('Erro de indíce')
except BaseException as ex:
    print('Erro desconhecido. Erro {}' .format(ex))