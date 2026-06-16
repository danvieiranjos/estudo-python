#criando programa de ping simples
import os

print("#" * 60)
#recebendo os dados
ip_ou_host = input("Digite o IP ou Host: ")
print("-" * 60)
#executando o ping
os.system('ping -n 6 {}' .format(ip_ou_host))
