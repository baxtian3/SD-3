#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys

for line in sys.stdin:
    # Convertir el texto a minúsculas
    line = line.lower()

    # Eliminar caracteres especiales
    for char in [",", ".", '"', "'", "(", ")", "\\", ";", ":", "$1", "$", "&"]:
        line = line.replace(char, '')

    # Dividir el texto en nombre y conjunto de documentos
    name, docs = line.split('<splittername>')

    # Procesar cada palabra en el conjunto de documentos
    for word in docs.split():
        # Imprimir el formato específico
        print('{}\t{}\t{}'.format(word, name, 1))
