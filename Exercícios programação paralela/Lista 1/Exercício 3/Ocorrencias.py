def contar_ocorrencias(texto):
  texto = texto.lower()

  palavras = texto.split()

  contagem = {}

  for palavra in palavras:
      contagem[palavra] = contagem.get(palavra, 0) + 1
  return contagem


texto = "O gato é preto. O cachorro é marrom. O pássaro é azul."
resultado = contar_ocorrencias(texto)
print("Contagem de ocorrências de cada palavra:")
for palavra, ocorrencias in resultado.items():
  print(f"{palavra}: {ocorrencias}")