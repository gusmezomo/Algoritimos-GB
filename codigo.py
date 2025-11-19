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



#analizar melhor essa parte


# função para achar o sub-retângulo de maior soma (força bruta)
def maior_subretangulo(matriz):
    n = len(matriz)
    melhor_soma = float('-inf')
    #('-inf') significa menos infinito
    #é usado quando você quer começar com um valor tão baixo
    #, tão ruim, que qualquer outra soma da matriz será maior do que ele

    melhor_subretangulo = None

    # Itera sobre todas as possíveis linhas iniciais do sub-retângulo.
    for linha_inicial in range(n):
        # Para cada linha inicial, itera sobre todas as possíveis linhas finais.
        # Começa de 'linha_inicial' para garantir que a linha final seja sempre igual ou posterior à inicial.
        for linha_final in range(linha_inicial, n):
            # Itera sobre todas as possíveis colunas iniciais do sub-retângulo.
            for coluna_inicial in range(n):
                # Para cada coluna inicial, itera sobre todas as possíveis colunas finais.
                # Começa de 'coluna_inicial' para garantir que a coluna final seja sempre igual ou posterior à inicial.
                for coluna_final in range(coluna_inicial, n):

                    sub = submatriz(matriz, linha_inicial, linha_final, coluna_inicial, coluna_final)

                    # soma dos elementos do sub-retângulo
                    soma = 0
                    for linha in sub:
                        for numero in linha:
                            soma += numero

                    if soma > melhor_soma:
                        melhor_soma = soma
    return melhor_soma, melhor_subretangulo


# executar e mostrar somente resultado final
melhor_soma, melhor_subretangulo = maior_subretangulo(matriz)

print("Maior soma encontrada:", melhor_soma)
print("Sub-retângulo correspondente:")
for linha in melhor_subretangulo:
    print(linha)