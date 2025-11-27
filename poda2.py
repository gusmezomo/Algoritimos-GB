#mudanca minima na poda2 para poda

import time

def max_subrectangle_podado_seguro(matrix):
    n = len(matrix)
    if n == 0:
        return 0

    max_sum = float('-inf')
    max_cell = max(max(row) for row in matrix) if any(matrix) else 0
    use_maxcell = max_cell > 0  # evita checagens repetidas

    poda2_ocorreu = False
    poda3_ocorreu = False

    for top in range(n):
        for left in range(n):
            for bottom in range(top, n):
                height = bottom - top + 1
                for right in range(left, n):

                    width = right - left + 1
                    area = width * height

                    # PODA 2
                    if use_maxcell:
                        if max_cell * area < max_sum:
                            poda2_ocorreu = True
                            continue

                    current = 0
                    cells_left = area
                    abort = False

                    for i in range(top, bottom + 1):
                        row = matrix[i]
                        for j in range(left, right + 1):
                            current += row[j]
                            cells_left -= 1

                            if use_maxcell:
                                possible_upper = current + cells_left * max_cell
                                if possible_upper < max_sum:
                                    poda3_ocorreu = True
                                    abort = True
                                    break

                        if abort:
                            break

                    if (not abort) and current > max_sum:
                        max_sum = current

    print("Poda 2 foi utilizada." if poda2_ocorreu else "Poda 2 não foi utilizada.")
    print("Poda 3 foi utilizada." if poda3_ocorreu else "Poda 3 não foi utilizada.")

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
    file_path = 'in_out/in1'
    matrix = read_matrix_from_file(file_path)

    start_time = time.time()
    result = max_subrectangle_podado_seguro(matrix)
    end_time = time.time()

    print(f"The maximum subrectangle sum is: {result}")
    print(f"Execution time: {end_time - start_time:.5f} seconds")