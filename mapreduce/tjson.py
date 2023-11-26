import json

def convertir_a_json(archivo_txt, archivo_json):
    # Diccionario para almacenar el índice invertido
    indice_invertido = {}

    # Leer el archivo de texto y procesar cada línea
    with open(archivo_txt, 'r', encoding='utf-8') as f:
        for linea in f:
            # Dividir la línea en partes utilizando espacios o tabs como separadores
            palabra_clave, *pares = linea.strip().split()

            # Procesar los pares (documento, frecuencia)
            atributos = {str(doc): freq for doc, freq in (map(int, par.strip('()').split(',')) for par in pares if par.strip('()'))}

            # Agregar la palabra clave y sus atributos al índice invertido
            indice_invertido[palabra_clave] = atributos

    # Escribir el índice invertido en formato JSON
    with open(archivo_json, 'w', encoding='utf-8') as f_json:
        json.dump(indice_invertido, f_json, ensure_ascii=False, indent=2)

    print(f'JSON completo: {archivo_json}')

# Llamar a la función con las rutas de los archivos
convertir_a_json('part-00000', 'indice_invertido.json')

