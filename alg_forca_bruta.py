#le a matriz de um arquivo de texto
matriz = []

# Abre o arquivo
with open("in_out/in2", "r") as arquivo:
    # Lê o tamanho
    n = int(arquivo.readline().strip())
    # Lê as próximas n linhas
    for _ in range(n):
        linha = list(map(int, arquivo.readline().split()))
        matriz.append(linha)

#função que cria um subretangulo
def submatriz(matriz, linha_inicial, linha_final, coluna_inicial, coluna_final):
    return [linha[coluna_inicial:coluna_final+1] for linha in matriz[linha_inicial:linha_final+1]]

# função para achar o sub-retângulo de maior soma
def maior_subretangulo(matriz):
    #tamanho da matriz : 5x5 10x10 etc
    tamanho_matriz = len(matriz)
    # Inicializa com o primeiro elemento da matriz.
    melhor_soma = matriz[0][0]

    # escolhendo cada linha onde o retângulo pode começar
    for linha_inicial in range(tamanho_matriz):
        # escolhendo onde essa linha vai terminar (sempre depois ou igual à inicial)
        for linha_final in range(linha_inicial, tamanho_matriz):
            # escolhendo onde o retângulo começa na horizontal
            for coluna_inicial in range(tamanho_matriz):
                # escolhendo onde ele termina
                for coluna_final in range(coluna_inicial, tamanho_matriz):
                    # a função 'submatriz' é chamada para extrair o sub-retângulo correspondente.
                    subretangulo = submatriz(matriz, linha_inicial, linha_final, coluna_inicial, coluna_final)

                    #Soma dos elementos do sub-retângulo atual.
                    soma = 0
                    for linha in subretangulo:
                        for numero in linha:
                            soma += numero

                    # Compara a 'soma' do sub-retângulo atual com a 'melhor_soma' encontrada até o momento.
                    if soma > melhor_soma:
                        # Se a soma atual for maior, ela se torna a nova 'melhor_soma'.
                        melhor_soma = soma
                        
    # a função retorna a maior soma encontrada.
    return melhor_soma

# Chama a função 'maior_subretangulo', passando a matriz lida do arquivo.
melhor_soma = maior_subretangulo(matriz)

print("Maior soma encontrada:", melhor_soma)
