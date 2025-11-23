def ler_entrada(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        n = int(f.readline())
        m = []
        for _ in range(n):
            linha = list(map(int, f.readline().split()))
            m.append(linha)
    return m

def max_subrectangle_n5_original(mat):
    n = len(mat)
    best = -10**18

    # Pair of horizontal boundaries
    for top in range(n):
        for bottom in range(top, n):

            # Try every possible left column
            for left in range(n):
                # And every possible right column
                for right in range(left, n):

                    # Compute sum of full rectangle by scanning each cell
                    total = 0
                    for row in range(top, bottom + 1):
                        for col in range(left, right + 1):
                            total += mat[row][col]

                    if total > best:
                        best = total

    return best

if __name__ == "__main__":
    import sys
    import time
    # Se o nome do arquivo não foi passado como argumento, usa 'in_out/in2'
    if len(sys.argv) > 1:
        nome_arquivo = sys.argv[1]
    else:
        # Se não, usa um arquivo padrão, por exemplo 'in_out/in2'
        nome_arquivo = 'in_out/in1' 
    
    matriz = ler_entrada(nome_arquivo)
    
    inicio = time.time()
    resultado = max_subrectangle_n5_original(matriz)
    fim = time.time()
    
    print(f"A soma máxima do sub-retângulo é: {resultado}")
    print(f"Tempo de execução: {fim - inicio} segundos")