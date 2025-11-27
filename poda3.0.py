#le a matriz de um arquivo de entrada
matriz = []

# Abre o arquivo da matriz
with open("in_out/in2", "r") as arquivo:
    # Lê o tamanho
    n = int(arquivo.readline().strip())
    # Lê as próximas n linhas
    for _ in range(n):
        linha = list(map(int, arquivo.readline().split()))
        matriz.append(linha)

# função inicial para criar um subretangulo
def submatriz(matriz, linha_inicial, linha_final, coluna_inicial, coluna_final):
    return [linha[coluna_inicial:coluna_final+1] for linha in matriz[linha_inicial:linha_final+1]]

# função para achar o sub-retângulo de maior soma, com a adição da lógica de poda
def maior_subretangulo_com_poda(matriz):
    # tamanho da matriz : 5x5 10x10 etc
    tamanho_matriz = len(matriz)
    # Inicializa com o primeiro elemento da matriz.
    melhor_soma = matriz[0][0]

    # PRÉ-CÁLCULO PARA PODA: Calcula o máximo absoluto na matriz
    # É usado como um limite superior teórico para qualquer sub-retângulo.
    celula_maxima = max(max(linha) for linha in matriz) if any(matriz) else 0

    # Define a borda superior do sub-retângulo.
    for linha_inicial in range(tamanho_matriz):
        # Define a borda inferior do sub-retângulo.
        for linha_final in range(linha_inicial, tamanho_matriz):
            # Define a borda esquerda do sub-retângulo.
            for coluna_inicial in range(tamanho_matriz):
                # Define a borda direita do sub-retângulo.
                for coluna_final in range(coluna_inicial, tamanho_matriz):

                    # Cálculo de área para a poda
                    largura = coluna_final - coluna_inicial + 1
                    altura = linha_final - linha_inicial + 1
                    area = largura * altura

                    # PODA: Se o retângulo, mesmo com o maior valor da matriz
                    # em todas as células, não alcança a 'melhor_soma' já encontrada,
                    # ele não precisa ser calculado.
                    if celula_maxima > 0 and celula_maxima * area < melhor_soma:
                        continue # Pula para o próximo sub-retângulo

                    # Para a combinação atual de coordenadas, a função 'submatriz' é chamada
                    # para extrair o sub-retângulo correspondente.
                    subretangulo = submatriz(matriz, linha_inicial, linha_final, coluna_inicial, coluna_final)

                    # Soma dos elementos do sub-retângulo atual.
                    soma = 0
                    # Itera sobre cada 'linha' dentro do 'subretangulo'.
                    for linha in subretangulo:
                        # Dentro de cada linha, itera sobre cada 'numero'.
                        for numero in linha:
                            # Adiciona o valor do 'numero' à 'soma' total.
                            soma += numero

                    # Compara e atualiza a 'melhor_soma'.
                    if soma > melhor_soma:
                        melhor_soma = soma

    # retorna a maior soma encontrada.
    return melhor_soma

melhor_soma = maior_subretangulo_com_poda(matriz)
print("Maior soma encontrada:", melhor_soma)
