import time

def max_subrectangle_podado_seguro(matrix):
    n = len(matrix)
    if n == 0:
        return 0

    max_sum = float('-inf')
    # máximo absoluto na matriz (usado como bound por célula)
    max_cell = max(max(row) for row in matrix) if any(matrix) else 0

    poda2_ocorreu = False
    poda3_ocorreu = False

    for top in range(n):
        for left in range(n):
            for bottom in range(top, n):
                for right in range(left, n):

                    width = right - left + 1
                    height = bottom - top + 1
                    area = width * height

                    # PODA 1 + PODA 2 (antecipadas):
                    # se mesmo com max_cell em todas as células não alcança max_sum
                    # então não vale a pena processar o retângulo
                    if max_cell > 0 and max_cell * area < max_sum:
                        poda2_ocorreu = True
                        poda3_ocorreu = True
                        continue

                    current = 0

                    # varredura sem podas internas (muito mais rápida)
                    for i in range(top, bottom + 1):
                        for j in range(left, right + 1):
                            current += matrix[i][j]

                    if current > max_sum:
                        max_sum = current

    if poda2_ocorreu:
        print("Poda 1 foi utilizada.")
    else:
        print("Poda 1 não foi utilizada.")

    if poda3_ocorreu:
        print("Poda 2 foi utilizada.")
    else:
        print("Poda 2 não foi utilizada.")

    return max_sum


def read_matrix_from_file(file_path):
    with open(file_path, 'r') as f:
        n = int(f.readline())
        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            matrix.append(row)
    return matrix


if __name__ == "__main__":
    file_path = '/content/sample_data/in1'  # ajuste o caminho caso necessário
    matrix = read_matrix_from_file(file_path)

    start_time = time.time()
    result = max_subrectangle_podado_seguro(matrix)
    end_time = time.time()

    print(f"The maximum subrectangle sum is: {result}")
    print(f"Execution time: {end_time - start_time:.5f} seconds")
