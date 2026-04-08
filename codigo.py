import random
import time
import copy
import matplotlib.pyplot as plt

# ==============================
# BUBBLE SORT (O(n²))
# ==============================
def bubble_sort(v):
    n = len(v)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                trocou = True
        if not trocou:
            break


# ==============================
# HEAP SORT (O(n log n))
# ==============================
def heapify(v, n, i):
    maior = i
    esq = 2*i + 1
    dir = 2*i + 2

    if esq < n and v[esq] > v[maior]:
        maior = esq

    if dir < n and v[dir] > v[maior]:
        maior = dir

    if maior != i:
        v[i], v[maior] = v[maior], v[i]
        heapify(v, n, maior)


def heap_sort(v):
    n = len(v)

    for i in range(n//2 - 1, -1, -1):
        heapify(v, n, i)

    for i in range(n-1, 0, -1):
        v[i], v[0] = v[0], v[i]
        heapify(v, i, 0)


# ==============================
# GERAÇÃO DE VETORES
# ==============================
def vetor_aleatorio(n):
    return [random.randint(0, 10000) for _ in range(n)]

def vetor_ordenado(n):
    return list(range(n))

def vetor_inverso(n):
    return list(range(n, 0, -1))


# ==============================
# TESTE DE TEMPO
# ==============================
def testar(algoritmo, vetor):
    v = copy.copy(vetor)
    inicio = time.time()
    algoritmo(v)
    fim = time.time()
    return (fim - inicio) * 1000


# ==============================
# CONFIGURAÇÃO
# ==============================
tamanhos = [1000, 3000, 5000]
execucoes = 5

tipos = {
    "Aleatório": vetor_aleatorio,
    "Ordenado": vetor_ordenado,
    "Inverso": vetor_inverso
}

resultados = {}

print("=== INÍCIO DOS TESTES ===\n")

# ==============================
# EXECUÇÃO DOS TESTES
# ==============================
for tipo_nome, func_geradora in tipos.items():
    print(f"\n--- Testando: {tipo_nome} ---")
    
    bubble_resultados = []
    heap_resultados = []

    for n in tamanhos:
        tempos_bubble = []
        tempos_heap = []

        print(f"Tamanho {n}:")

        for i in range(execucoes):
            vetor = func_geradora(n)

            tempo_b = testar(bubble_sort, vetor)
            tempo_h = testar(heap_sort, vetor)

            tempos_bubble.append(tempo_b)
            tempos_heap.append(tempo_h)

            print(f"  Execução {i+1}: Bubble = {tempo_b:.2f} ms | Heap = {tempo_h:.2f} ms")

        media_b = sum(tempos_bubble) / execucoes
        media_h = sum(tempos_heap) / execucoes

        bubble_resultados.append(media_b)
        heap_resultados.append(media_h)

        print(f"→ MÉDIA: Bubble = {media_b:.2f} ms | Heap = {media_h:.2f} ms\n")

    resultados[tipo_nome] = (bubble_resultados, heap_resultados)


# ==============================
# GRÁFICOS
# ==============================
for tipo_nome, (bubble_resultados, heap_resultados) in resultados.items():
    plt.figure()

    plt.plot(tamanhos, bubble_resultados, marker='o', label='Bubble Sort')
    plt.plot(tamanhos, heap_resultados, marker='o', label='Heap Sort')

    plt.title(f"Desempenho - {tipo_nome}")
    plt.xlabel("Tamanho do vetor (n)")
    plt.ylabel("Tempo (ms)")

    plt.legend()
    plt.grid()

    plt.show()