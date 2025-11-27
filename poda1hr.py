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

                    # PODA 2 (segura): se mesmo com max_cell por célula não alcança max_sum
                    if max_cell > 0 and max_cell * area < max_sum:
                        poda2_ocorreu = True
                        continue

                    current = 0
                    abort = False

                    # varrendo as células na ordem linha->coluna
                    for i in range(top, bottom + 1):
                        for j in range(left, right + 1):
                            current += matrix[i][j]

                            # calcula quantas células ainda faltam (incluindo as que estão após j na linha corrente)
                            cells_already = (i - top) * width + (j - left + 1)
                            remaining = area - cells_already

                            # PODA 3 (segura quando usada corretamente):
                            # mesmo que todas as células restantes fossem = max_cell,
                            # soma final máxima possível seria:
                            if max_cell > 0:
                                possible_upper = current + remaining * max_cell
                                if possible_upper < max_sum:
                                    poda3_ocorreu = True
                                    abort = True
                                    break
                        if abort:
                            break

                    if not abort and current > max_sum:
                        max_sum = current

    if poda2_ocorreu:
        print("Poda 2 foi utilizada.")
    else:
        print("Poda 2 não foi utilizada.")

    if poda3_ocorreu:
        print("Poda 3 foi utilizada.")
    else:
        print("Poda 3 não foi utilizada.")

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
    # Example usage with the file 'in_out/in2'
    file_path = '/content/sample_data/in1'
    matrix = read_matrix_from_file(file_path)

    start_time = time.time()
    result = max_subrectangle_podado_seguro(matrix)
    end_time = time.time()

    print(f"The maximum subrectangle sum is: {result}")
    print(f"Execution time: {end_time - start_time:.5f} seconds")