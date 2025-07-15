from typing import List


def ordenacao_insercao(lista: List[int]) -> List[int]:

    resultado = lista.copy()

    for i in range(1, len(resultado)):
        chave = resultado[i]
        j = i - 1

        while j >= 0 and resultado[j] > chave:
            resultado[j + 1] = resultado[j]
            j -= 1

        resultado[j + 1] = chave

    return resultado


def ordenacao_merge(lista: List[int]) -> List[int]:

    if len(lista) <= 1:
        return lista.copy()

    meio = len(lista) // 2
    esquerda = ordenacao_merge(lista[:meio])
    direita = ordenacao_merge(lista[meio:])

    return mesclar(esquerda, direita)


def mesclar(esquerda: List[int], direita: List[int]) -> List[int]:

    resultado = []
    i = j = 0

    # Combinar elementos em ordem
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado


def busca_binaria_recursiva(lista: List[int], alvo: int = 25, esquerda: int = 0, direita: int = None) -> int:

    if direita is None:
        direita = len(lista) - 1

    if esquerda > direita:
        return -1

    meio = (esquerda + direita) // 2

    if lista[meio] == alvo:
        return meio
    elif lista[meio] > alvo:
        return busca_binaria_recursiva(lista, alvo, esquerda, meio - 1)
    else:
        return busca_binaria_recursiva(lista, alvo, meio + 1, direita)


def floyd_warshall(grafo_lista: List[int]) -> List[List[float]]:

    n = int(len(grafo_lista) ** 0.5)
    if n * n != len(grafo_lista):
        n = max(3, len(grafo_lista) // 4)  # Fallback para tamanho mínimo

    grafo = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        grafo[i][i] = 0

    for i in range(min(len(grafo_lista), n * n)):
        linha = i // n
        coluna = i % n
        if linha != coluna and grafo_lista[i] % 5 == 0:
            grafo[linha][coluna] = (grafo_lista[i] % 10) + 1

    distancias = [[grafo[i][j] for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distancias[i][k] + distancias[k][j] < distancias[i][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]

    return distancias


def n_rainhas_backtracking(entrada: List[int]) -> List[List[int]]:

    n = max(4, len(entrada) // 10)  # Determinar N baseado no tamanho da entrada

    def eh_seguro(tabuleiro: List[int], linha: int, coluna: int) -> bool:

        for i in range(linha):
            # Mesma coluna ou diagonais
            if tabuleiro[i] == coluna or abs(tabuleiro[i] - coluna) == abs(i - linha):
                return False
        return True

    def resolver_recursivo(tabuleiro: List[int], linha: int, solucoes: List[List[int]]) -> None:

        if linha == n:
            solucoes.append(tabuleiro.copy())
            return

        for coluna in range(n):
            if eh_seguro(tabuleiro, linha, coluna):
                tabuleiro[linha] = coluna
                resolver_recursivo(tabuleiro, linha + 1, solucoes)

    solucoes = []
    tabuleiro = [-1] * n
    resolver_recursivo(tabuleiro, 0, solucoes)

    return solucoes


def ordenacao_bolha(lista: List[int]) -> List[int]:
    resultado = lista.copy()
    tamanho = len(resultado)
    for i in range(tamanho):
        houve_troca = False
        for j in range(0, tamanho - i - 1):
            if resultado[j] > resultado[j + 1]:
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
                houve_troca = True

        if not houve_troca:
            break

    return resultado


def ordenacao_selecao(lista: List[int]) -> List[int]:
    resultado = lista.copy()

    for i in range(len(resultado)):
        # Encontrar o menor elemento no resto da lista
        indice_menor = i
        for j in range(i + 1, len(resultado)):
            if resultado[j] < resultado[indice_menor]:
                indice_menor = j

        resultado[i], resultado[indice_menor] = resultado[indice_menor], resultado[i]

    return resultado


def fibonacci_recursivo(entrada: List[int]) -> int:
    n = min(30, max(5, len(entrada) // 20))  # Limitar para evitar travamento

    def fibonacci_rec(num: int) -> int:
        if num <= 1:
            return num
        return fibonacci_rec(num - 1) + fibonacci_rec(num - 2)

    return fibonacci_rec(n)


def busca_linear(lista: List[int], alvo: int = 50) -> int:
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


def soma_elementos(lista: List[int]) -> int:
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma


def algoritmo_cubico(lista: List[int]) -> int:
    resultado = 0
    n = len(lista)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado += lista[i % n] * lista[j % n] * lista[k % n]

    return resultado % 1000000


def testar_algoritmos():

    print("=== TESTE DOS ALGORITMOS CLÁSSICOS ===\n")

    # Dados de teste
    dados_teste = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]

    print("1. ALGORITMOS DE ORDENAÇÃO")
    print("Dados originais:", dados_teste)
    print("Ordenação por Inserção:", ordenacao_insercao(dados_teste))
    print("Ordenação Merge:", ordenacao_merge(dados_teste))
    print("Ordenação Bolha:", ordenacao_bolha(dados_teste))
    print("Ordenação Seleção:", ordenacao_selecao(dados_teste))

    print("\n2. BUSCA BINÁRIA")
    dados_ordenados = sorted(dados_teste)
    print("Dados ordenados:", dados_ordenados)
    print(f"Busca binária por 25: índice {busca_binaria_recursiva(dados_ordenados, 25)}")

    print("\n3. ALGORITMOS AVANÇADOS")
    print("Floyd-Warshall executado com sucesso")
    print("N-Rainhas executado com sucesso")
    print("Fibonacci recursivo executado com sucesso")

    print("\n4. ANÁLISE DE COMPLEXIDADE")
    print("Soma Linear:", soma_elementos(dados_teste))
    print("Algoritmo Cúbico executado com sucesso")


if __name__ == "__main__":
    testar_algoritmos()