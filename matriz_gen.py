import random

def gerar_matriz_txt():
    # Pede o tamanho da matriz
    N = int(input("Digite o tamanho da matriz (N): "))

    # Nome do arquivo
    nome_arquivo = "m_gerada.txt"

    # Gera a matriz NxN com valores entre -127 e 127
    matriz = [[random.randint(-127, 127) for _ in range(N)] for _ in range(N)]

    # Salva no arquivo
    with open(nome_arquivo, "w") as f:
        f.write(str(N) + "\n")
        for linha in matriz:
            f.write(" ".join(map(str, linha)) + "\n")

    print(f"\nMatriz {N}x{N} gerada e salva em '{nome_arquivo}' com sucesso!")

# Executa
gerar_matriz_txt()
