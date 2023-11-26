import json

def cargar_json(ruta_json):
    with open(ruta_json, 'r', encoding='utf-8') as f:
        return json.load(f)

def buscar_en_indice(query, indice):
    resultados = {}

    # Utilizar get() para manejar el caso en que la palabra clave no está en el índice
    for documento, frecuencia in indice.get(query, {}).items():
        resultados[documento] = resultados.get(documento, 0) + frecuencia

    # Ordenar los resultados por relevancia (mayor a menor)
    resultados_ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)

    # Devolver los primeros 5 resultados
    return resultados_ordenados[:5]

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

# Ruta del archivo JSON con el índice invertido
ruta_json = 'indice_invertido.json'

# Cargar el índice invertido desde el archivo JSON
indice_invertido = cargar_json(ruta_json)

# Consulta del usuario
consulta_usuario = input("Buscar: ")

# Realizar la búsqueda
resultados_busqueda = buscar_en_indice(consulta_usuario, indice_invertido)

# Mostrar los resultados
if resultados_busqueda:
    print("\nMejores resultados:")
    url_base = 'https://es.wikipedia.org/wiki/'
    for documento, puntaje in resultados_busqueda:
        url = url_base + entradas[int(documento) - 1]
        print(f'Documento: {documento}, Frecuencia: {puntaje}, URL: {url}')
else:
    print("No se encontraron resultados para la consulta.")
