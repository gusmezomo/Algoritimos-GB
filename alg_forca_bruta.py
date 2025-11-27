#le a matriz de um arquivo de texto
matriz = []

# Abre o arquivo
with open("in_out/gen25.txt", "r") as arquivo:
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

#OBS FUNÇAO ATUAL RETORNA APENAS O RESULTADO DA MAIOR SOMA, NAO O SUB-RETANGULO EM SI

# função para achar o sub-retângulo de maior soma
def maior_subretangulo(matriz):
    #tamanho da matriz : 5x5 10x10 etc
    tamanho_matriz = len(matriz)
    # Inicializa com o primeiro elemento da matriz.
    melhor_soma = matriz[0][0]

    # Itera sobre todas as possíveis linhas iniciais do sub-retângulo.
    for linha_inicial in range(tamanho_matriz):
        # Para cada linha inicial, itera sobre todas as possíveis linhas finais.
        # Começa de 'linha_inicial' para garantir que a linha final seja sempre igual ou posterior à inicial.
        for linha_final in range(linha_inicial, tamanho_matriz):
            # Itera sobre todas as possíveis colunas iniciais do sub-retângulo.
            for coluna_inicial in range(tamanho_matriz):
                # Para cada coluna inicial, itera sobre todas as possíveis colunas finais.
                # Começa de 'coluna_inicial' para garantir que a coluna final seja sempre igual ou posterior à inicial.
                for coluna_final in range(coluna_inicial, tamanho_matriz):
                    # Para a combinação atual de coordenadas (linha_inicial, linha_final, etc.),
                    # a função 'submatriz' é chamada para extrair o sub-retângulo correspondente da matriz principal.
                    subretangulo = submatriz(matriz, linha_inicial, linha_final, coluna_inicial, coluna_final)

                    # Inicia uma variável 'soma' para calcular a soma dos elementos do sub-retângulo atual.
                    soma = 0
                    # Itera sobre cada 'linha' dentro do 'subretangulo' (sub-retângulo).
                    for linha in subretangulo:
                        # Dentro de cada linha, itera sobre cada 'numero'.
                        for numero in linha:
                            # Adiciona o valor do 'numero' à 'soma' total do sub-retângulo.
                            soma += numero

                    # Compara a 'soma' do sub-retângulo atual com a 'melhor_soma' encontrada até o momento.
                    if soma > melhor_soma:
                        # Se a soma atual for maior, ela se torna a nova 'melhor_soma'.
                        melhor_soma = soma
                        
    # Após todos os laços terminarem (ou seja, todos os sub-retângulos foram verificados),
    # a função retorna a maior soma encontrada e o sub-retângulo correspondente.
    return melhor_soma

# --- Execução do Código ---
# Chama a função 'maior_subretangulo', passando a matriz lida do arquivo.
# Os valores retornados (a maior soma) são armazenados nas variáveis.
melhor_soma = maior_subretangulo(matriz)

print("Maior soma encontrada:", melhor_soma)
