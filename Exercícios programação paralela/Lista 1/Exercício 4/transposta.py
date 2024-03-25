import numpy as np

def calcular_transposta(matriz):
    # Calcula a transposta da matriz usando numpy.transpose()
    matriz_transposta = np.transpose(matriz)
    return matriz_transposta

# Exemplo de utilização da função
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

transposta = calcular_transposta(matriz)
print("Matriz original:")
print(matriz)
print("\nTransposta da matriz:")
print(transposta)