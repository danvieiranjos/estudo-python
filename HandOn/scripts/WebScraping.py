import requests
import pandas as pd
from bs4 import BeautifulSoup



req = requests.get('https://s2group1.sharepoint.com/sites/InFiles/Documentos%20Compartilhados/Departamento%20Pessoal/Administrativo%20-%20RH/PRONTUÁRIO%20DO%20COLABORADOR/Sergio%20Brunetta%20Junior/INSS.pdf')
print(response.status_code)
print(response.text)