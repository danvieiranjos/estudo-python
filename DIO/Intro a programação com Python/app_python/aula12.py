import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/' .format(cep))
    print(response.status_code)
    print(response.text)
    print(response.json())

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/' .format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

if __name__ == '__main__':
    retorna_dados_cep('42711820')
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon)