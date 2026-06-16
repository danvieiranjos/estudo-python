import os
import time
#abrindo o arquivo host
with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print("Verificando IP: " , ip)
        print('-' * 60)
        os.system('ping -n 2 {}' .format(ip))
        print("._." * 20)
        time.sleep(5)

