#DIOScanner é um projeto dedicado ao treinamento por Bruno Dias
# Seu uso e edição é permitido desde que citado o autor
#brunocdias@live.com

import nmap

scanner = nmap.PortScanner()

print("Seja bem vindo ao DIOScanner")
print("<-------------------------->")

ip = input("Digite o ip  a ser varrido..." , end=' ')
print("O IP digitado foi: ", ip)
type (ip)

menu = input("""\n Escolha o tipo de varredura a ser realizada
                1-> Varredura do Tipo SYN
                2-> Varredura do Tipo UDP
                3-> Varredura do Tipo Intensa
                Digite a opção escolhida: """)

print("A opção foi: " , menu)

if menu == "1":
    print("Versao do NMAP: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())
elif menu == "2":
    print("Versao do NMAP: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['udp'].keys())
elif menu == "3":
    print("Versao do NMAP: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sC')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())
