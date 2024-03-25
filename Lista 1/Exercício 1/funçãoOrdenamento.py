import numpy

def ordenar_vetor(vetor):

    vetor_ordenado = numpy.sort(vetor)
    return vetor_ordenado


vetor = [3, 1, 4, 1, 5, 9, 2, 6, 5]
vetor_ordenado = ordenar_vetor(vetor)
print("Vetor original:", vetor)
print("Vetor ordenado:", vetor_ordenado)