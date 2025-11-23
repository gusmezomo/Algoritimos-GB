def ler_entrada(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        n = int(f.readline())
        m = []
        for _ in range(n):
            linha = list(map(int, f.readline().split()))
            m.append(linha)
    return m

def max_subrectangle(m):
    n = len(m)
    best = -10**18

    # Percorre coluna esquerda
    for left in range(n):
        # cria um vetor acumulador de linhas
        acc = [0] * n

        # avança a fronteira direita
        for right in range(left, n):

            # soma coluna atual no acumulador
            for row in range(n):
                acc[row] += m[row][right]

            # agora precisamos testar todos os retângulos que usam esta faixa de colunas
            # fazemos isso escolhendo topo e base
            curr_sum = 0

            # varre topo → bottom implicitamente
            for bottom in range(n):
                curr_sum += acc[bottom]
                if curr_sum > best:
                    best = curr_sum
                # reinicia soma se for ruim
                if curr_sum < 0:
                    curr_sum = 0

    return best

if __name__ == "__main__":
    import sys
    # Se o nome do arquivo não foi passado como argumento, usa 'in_out/in2'
    if len(sys.argv) > 1:
        nome_arquivo = sys.argv[1]
    else:
        # Se não, usa um arquivo padrão, por exemplo 'in_out/in2'
        nome_arquivo = 'in_out/in1' 
    
    matriz = ler_entrada(nome_arquivo)
    resultado = max_subrectangle(matriz)
    print(f"A soma máxima do sub-retângulo é: {resultado}")