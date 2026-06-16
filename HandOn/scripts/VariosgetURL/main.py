import csv
import requests

with open("teste.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    print("Start")

    for row in csv_reader:
        url = row["url"]
        req = requests.get(url, timeout=5)

        if req.status_code == 200:
            found = "Acesso necessário" in str(req.content)
            print(f"{url} esta bloqueado: {found}")
        else:
            print(f"erro ao consultar {url}")

    print("End")
