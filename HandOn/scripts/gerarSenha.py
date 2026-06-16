# Programa para gerar senhas aleatorias
# Danilo Vieira

import random
passlen = int(input("Digite o tamanho da senha: "))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
senha = "".join(random.sample(s,passlen))
print (senha)
