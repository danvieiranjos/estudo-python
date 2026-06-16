# Simulator de dado
# Danilo Vieira
# 15/07/2021

import random
while True:
    print(''' 1. Iniciar              2. Sair     ''')
    user = int(input("Escolha uma das opcoes... \n"))
    if user==1:
        number = random.randint(1,6)
        print(number)
    else:
        break
