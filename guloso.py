#codigo guloso, nao garante sucesso em todos os casos

def melhor_retangulo_expansivo(matriz):
    n = len(matriz)
    max_soma_global = -10**18  # muito negativo para iniciar

    # Função auxiliar: soma de uma linha entre duas colunas
    def soma_linha(linha, c1, c2):
        total = 0
        for c in range(c1, c2 + 1):
            total += matriz[linha][c]
        return total

    # Função auxiliar: soma de uma coluna entre duas linhas
    def soma_coluna(coluna, r1, r2):
        total = 0
        for r in range(r1, r2 + 1):
            total += matriz[r][coluna]
        return total

    # Testamos iniciar o retângulo em cada célula da matriz
    for i in range(n):
        for j in range(n):

            # Retângulo inicial = célula única
            linha_sup = i
            linha_inf = i
            col_esq = j
            col_dir = j
            soma_atual = matriz[i][j]

            while True:
                melhor_ganho = 0
                melhor_movimento = None

                # 1) Expandir para cima
                if linha_sup > 0:
                    ganho = soma_linha(linha_sup - 1, col_esq, col_dir)
                    if ganho > melhor_ganho:
                        melhor_ganho = ganho
                        melhor_movimento = "cima"

                # 2) Expandir para baixo
                if linha_inf < n - 1:
                    ganho = soma_linha(linha_inf + 1, col_esq, col_dir)
                    if ganho > melhor_ganho:
                        melhor_ganho = ganho
                        melhor_movimento = "baixo"

                # 3) Expandir para esquerda
                if col_esq > 0:
                    ganho = soma_coluna(col_esq - 1, linha_sup, linha_inf)
                    if ganho > melhor_ganho:
                        melhor_ganho = ganho
                        melhor_movimento = "esquerda"

                # 4) Expandir para direita
                if col_dir < n - 1:
                    ganho = soma_coluna(col_dir + 1, linha_sup, linha_inf)
                    if ganho > melhor_ganho:
                        melhor_ganho = ganho
                        melhor_movimento = "direita"

                # Se nenhuma expansão melhora a soma, paramos
                if melhor_ganho <= 0 or melhor_movimento is None:
                    break

                # Caso contrário, aplicamos a melhor expansão
                if melhor_movimento == "cima":
                    linha_sup -= 1
                elif melhor_movimento == "baixo":
                    linha_inf += 1
                elif melhor_movimento == "esquerda":
                    col_esq -= 1
                elif melhor_movimento == "direita":
                    col_dir += 1

                soma_atual += melhor_ganho

            # Atualiza melhor soma global
            if soma_atual > max_soma_global:
                max_soma_global = soma_atual

    return max_soma_global


# ------------------------------
# Leitura da entrada e execução
# ------------------------------
if __name__ == "__main__":
    file_path = 'in_out/in1'
    with open(file_path, 'r') as f:
        N = int(f.readline().strip())
        matriz = []
        for _ in range(N):
            linha = list(map(int, f.readline().split()))
            matriz.append(linha)

    resultado = melhor_retangulo_expansivo(matriz)
    print(resultado)