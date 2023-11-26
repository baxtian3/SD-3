import requests
import json

entradas = [
    "Seguridad Informática", 
    "Inteligencia artificial", 
    "Desarrollo web",
    "Base de datos",
    "Lenguaje de programación", 
    "Álgebra", 
    "Geometría", 
    "Cálculo",
    "Teoría de números", 
    "Mecánica cuántica",
    "Relatividad general",
    "Teoría de cuerdas",
    "Física de partículas",
    "Interacciones fundamentales",
    "Khea",
    "Paulo Londra",
    "Eladio Carrión",
    "Bad Bunny",
    "Anuel AA",
    "Cristiano Ronaldo",
    "Lionel Messi",
    "Michael Jackson",
    "Breaking Bad",
    "Interstellar",
    "Piano",
    "Usain Bolt",
    "Chile",
    "Estrella",
    "Agujero negro",
    "Tiempo"
]

url = "https://es.wikipedia.org/w/api.php"
i = 1
for entrada in entradas:
    entradaf = entrada.replace(" ", "_")
    params = {
        'format': 'json',
        'action': 'query',
        'prop': 'extracts',
        'exintro': '',
        'explaintext': '',
        'redirects': 1,
        'titles': entrada
    }

    req = requests.get(
        url,
        params=params
    ).json()

    n_page = list(req['query']['pages'].keys())[0]
    texto = req['query']['pages'][n_page]['extract']
    texto = '{}<splittername>{}'.format(i, json.dumps(texto))

    if i <= 15:
        with open(f'../carpeta1/{entradaf}.txt', 'w') as f:
            f.write(texto)
    else:
        with open(f'../carpeta2/{entradaf}.txt', 'w') as f:
            f.write(texto)
    i = i + 1

