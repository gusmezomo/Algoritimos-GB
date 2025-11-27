## Algoritmos Implementados

### 1. Força Bruta (`alg_forca_bruta.py`)

Este codigo implementa a solução de força bruta. Ele testa todas as sub-matrizes possíveis, calcula a soma de cada uma e retorna a maior soma encontrada.

### 2. Algoritmo com Poda (`alg_poda.py`)

Este codigo utiliza uma técnica de poda para melhorar a eficiência. A poda consiste em evitar o cálculo da soma de sub-retângulos que não têm potencial para superar a maior soma já encontrada.

## Estrutura do Projeto

-   `alg_forca_bruta.py`: Implementação do algoritmo de força bruta.
-   `alg_poda.py`: Implementação do algoritmo com poda.
-   `matriz_gen.py`: Um script feito com IA para gerar matrizes de teste.
-   `in_out/`: Pasta contendo os arquivos de entrada (matrizes) e os resultados de saída esperados.

## Como Executar

Para executar os algoritmos, você precisa modificar o script para apontar para o arquivo de entrada desejado.

### Exemplo de Execução

1.  Abra o arquivo `alg_forca_bruta.py` ou `alg_poda.py`.
2.  Localize a seguinte linha de código (geralmente na linha 5):

    ```python
    with open("in_out/in2", "r") as arquivo:
    ```

3.  Altere o caminho do arquivo (por exemplo, `"in_out/in2"`) para o arquivo de matriz que você deseja usar (ex: `"in_out/in1"`, `"in_out/gen25.txt"`, etc.).
4.  Execute o script Python a partir do seu terminal:

    ```sh
    python alg_forca_bruta.py
    ```

    ou

    ```sh
    python alg_poda.py
    ```
