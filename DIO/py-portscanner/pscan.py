#Programa criado por Danilo Vieira para aula de Python
#Licença para uso e edição desde que citado o autor Bruno Dias
#danilo.vieiranjos@gmail.com

import socket
print("Digite um host ou IP conforme exemplo")
ip = input("Ex.: google.com ou 8.4.2.1: ")

ports = []
count = 0
while count <10:
    ports.append(int(input(f"Digite a porta a ser verificada {count+1} de 10: ")))
    count +=1

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))

    if code == 0:
        print(str(port) , "-> Porta Aberta")
    else:
        print(str(port) , "-> Porta Fechada")

print("\n -> finish scan!!")