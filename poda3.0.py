# função inicial para criar um subretangulo (mantendo a estrutura do codigo.py)
def submatriz(matriz, linha_inicial, linha_final, coluna_inicial, coluna_final):
    return [linha[coluna_inicial:coluna_final+1] for linha in matriz[linha_inicial:linha_final+1]]

# função para achar o sub-retângulo de maior soma, com a adição da lógica de poda
def maior_subretangulo_com_poda(matriz):
    # tamanho da matriz : 5x5 10x10 etc (mantendo a estrutura do codigo.py)
    tamanho_matriz = len(matriz)
    if tamanho_matriz == 0:
        return 0

    # 1. PRÉ-CÁLCULO PARA PODA: Calcula o máximo absoluto na matriz (do podas2.0.py)
    # É usado como um limite superior teórico para qualquer sub-retângulo.
    max_cell = max(max(row) for row in matriz) if any(matriz) else 0

    # Inicializa com o primeiro elemento da matriz. (mantendo a estrutura do codigo.py)
    melhor_soma = matriz[0][0]

    # Itera sobre todas as possíveis linhas iniciais do sub-retângulo.
    for linha_inicial in range(tamanho_matriz):
        # Para cada linha inicial, itera sobre todas as possíveis linhas finais.
        for linha_final in range(linha_inicial, tamanho_matriz):
            # Itera sobre todas as possíveis colunas iniciais do sub-retângulo.
            for coluna_inicial in range(tamanho_matriz):
                # Para cada coluna inicial, itera sobre todas as possíveis colunas finais.
                for coluna_final in range(coluna_inicial, tamanho_matriz):

                    # Cálculo de área para a poda (do podas2.0.py)
                    width = coluna_final - coluna_inicial + 1
                    height = linha_final - linha_inicial + 1
                    area = width * height

                    # 2. PODA: Se o retângulo, mesmo com o maior valor da matriz
                    # em todas as células, não alcança a 'melhor_soma' já encontrada,
                    # ele não precisa ser calculado (do podas2.0.py).
                    if max_cell > 0 and max_cell * area < melhor_soma:
                        continue # Pula para o próximo sub-retângulo

                    # Para a combinação atual de coordenadas, a função 'submatriz' é chamada
                    # para extrair o sub-retângulo correspondente (mantendo a estrutura do codigo.py).
                    subretangulo = submatriz(matriz, linha_inicial, linha_final, coluna_inicial, coluna_final)

                    # Inicia uma variável 'soma' para calcular a soma dos elementos (mantendo a estrutura do codigo.py).
                    soma = 0
                    # Itera sobre cada 'linha' dentro do 'subretangulo'.
                    for linha in subretangulo:
                        # Dentro de cada linha, itera sobre cada 'numero'.
                        for numero in linha:
                            # Adiciona o valor do 'numero' à 'soma' total.
                            soma += numero

                    # Compara e atualiza a 'melhor_soma' (mantendo a estrutura do codigo.py).
                    if soma > melhor_soma:
                        melhor_soma = soma

    # Após todos os laços terminarem, a função retorna a maior soma encontrada.
    return melhor_soma

# --- Parte de leitura e execução (Adaptação do codigo.py) ---

#le a matriz de um arquivo de texto
matriz = []

# Abre o arquivo (mantendo o caminho do codigo.py)
# NOTA: O arquivo "in_out/gen25.txt" precisa estar acessível para esta parte funcionar
try:
    with open("in_out/gen25.txt", "r") as arquivo:
        # Lê o tamanho
        n = int(arquivo.readline().strip())
        # Lê as próximas n linhas
        for _ in range(n):
            linha = list(map(int, arquivo.readline().split()))
            matriz.append(linha)

    # Chama a função 'maior_subretangulo_com_poda', passando a matriz lida do arquivo.
    melhor_soma = maior_subretangulo_com_poda(matriz)
    print("Maior soma encontrada:", melhor_soma)

except FileNotFoundError:
    print("ERRO: Arquivo 'in_out/gen25.txt' não encontrado. Não foi possível executar o código com o arquivo.")
    print("Certifique-se de que o arquivo está no caminho correto.")