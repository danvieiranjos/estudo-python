# lista = [1, 2, 3, 4, 5]
# tupla = (10,11,12,13)
# outro = {1,2,3,4,5}
# # print (type(lista))
# # print(type(tupla))
# # print(type(outro))
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
#     print(soma)


lista_animal = ['lobo', 'cão', 'gato', 'cavalo']

if 'lobo' in lista_animal:
    print("Existe lobo na lista")
else:
    print("Não existe um lobo na lista")

print("Existe",lista_animal.count('lobo'), ", na lista")