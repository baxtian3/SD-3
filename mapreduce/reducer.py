#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys

current_word = None
current_doc_counts = {}

# Iteración sobre las líneas de entrada provenientes de los mappers
for line in sys.stdin:
    # Procesamiento de cada línea
    word, doc, count = line.strip().split('\t')
    count = int(count)

    # Verificación si la palabra actual es la misma que la anterior
    if current_word == word:
        current_doc_counts[doc] = current_doc_counts.get(doc, 0) + count
    else:
        # Imprimir resultados para la palabra anterior
        if current_word:
            doc_count_str = " ".join(f"({d},{c})" for d, c in current_doc_counts.items())
            print(f"{current_word}\t{doc_count_str}")

        # Actualizar la palabra y el diccionario de recuentos
        current_word = word
        current_doc_counts = {doc: count}

# Imprimir resultados para la última palabra
if current_word:
    doc_count_str = " ".join(f"({d},{c})" for d, c in current_doc_counts.items())
    print(f"{current_word}\t{doc_count_str}")
