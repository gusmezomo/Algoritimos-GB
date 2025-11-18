#le a matriz de um arquivo de texto
matriz = []

# Abre o arquivo
with open("input.txt", "r") as arquivo:
    # Lê o tamanho
    n = int(arquivo.readline().strip())
    # Lê as próximas n linhas
    for _ in range(n):
        linha = list(map(int, arquivo.readline().split()))
        matriz.append(linha)

# Exibir matriz
#for linha in matriz:
    #print(linha)

#função inicial para criar um subretangulo
def submatriz(matriz, linha_inicial, linha_final, coluna_inicial, coluna_final):
    return [linha[coluna_inicial:coluna_final+1] for linha in matriz[linha_inicial:linha_final+1]]

#exemplo do subretangulo maximo do exemplo do pdf
subretangulo = submatriz(matriz, 1, 3, 0, 1)
print(subretangulo)

#calcula a soma dos elementos do subretangulo
soma = 0
for linha in subretangulo:
    for numero in linha:
        soma += numero

print("Soma =", soma)