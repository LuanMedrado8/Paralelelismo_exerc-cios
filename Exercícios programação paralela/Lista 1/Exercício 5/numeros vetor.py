def contar_numeros(vetor):
    positivos = 0
    negativos = 0
    zeros = 0

    for numero in vetor:
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            zeros += 1
    
    return positivos, negativos, zeros


def ler_vetor():
    vetor = []
    n = int(input("Digite o tamanho do vetor: "))
    print("Digite os elementos do vetor:")
    for i in range(n):
        elemento = int(input())
        vetor.append(elemento)
    return vetor


vetor = ler_vetor()
positivos, negativos, zeros = contar_numeros(vetor)
print("Quantidade de números positivos:", positivos)
print("Quantidade de números negativos:", negativos)
print("Quantidade de zeros:", zeros)