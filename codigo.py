import copy
import csv
import os
import random
import time
from pathlib import Path


RANDOM_SEED = 42
TAMANHOS = [1000, 3000, 5000]
EXECUCOES = 5
RESULTADOS_CSV = Path("resultados.csv")


# ==============================
# BUBBLE SORT (O(n^2))
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
    esq = 2 * i + 1
    dir = 2 * i + 2

    if esq < n and v[esq] > v[maior]:
        maior = esq

    if dir < n and v[dir] > v[maior]:
        maior = dir

    if maior != i:
        v[i], v[maior] = v[maior], v[i]
        heapify(v, n, maior)


def heap_sort(v):
    n = len(v)

    for i in range(n // 2 - 1, -1, -1):
        heapify(v, n, i)

    for i in range(n - 1, 0, -1):
        v[i], v[0] = v[0], v[i]
        heapify(v, i, 0)


# ==============================
# GERACAO DE VETORES
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
    esperado = sorted(vetor)

    inicio = time.perf_counter()
    algoritmo(v)
    fim = time.perf_counter()

    if v != esperado:
        raise ValueError(f"{algoritmo.__name__} nao ordenou o vetor corretamente")

    return (fim - inicio) * 1000


def executar_experimentos(tamanhos=None, execucoes=EXECUCOES):
    tamanhos = tamanhos or TAMANHOS
    random.seed(RANDOM_SEED)

    tipos = {
        "Aleatorio": vetor_aleatorio,
        "Ordenado": vetor_ordenado,
        "Inverso": vetor_inverso,
    }

    algoritmos = {
        "Bubble Sort": bubble_sort,
        "Heap Sort": heap_sort,
    }

    resultados = []

    print("=== INICIO DOS TESTES ===\n")

    for tipo_nome, func_geradora in tipos.items():
        print(f"--- Testando: {tipo_nome} ---")

        for n in tamanhos:
            for algoritmo_nome, algoritmo in algoritmos.items():
                tempos = []

                for execucao in range(1, execucoes + 1):
                    vetor = func_geradora(n)
                    tempo_ms = testar(algoritmo, vetor)
                    tempos.append(tempo_ms)

                    resultados.append(
                        {
                            "tipo_vetor": tipo_nome,
                            "tamanho": n,
                            "algoritmo": algoritmo_nome,
                            "execucao": execucao,
                            "tempo_ms": tempo_ms,
                        }
                    )

                media = sum(tempos) / len(tempos)
                print(f"{tipo_nome:9} | n={n:5} | {algoritmo_nome:11} | media={media:8.3f} ms")

        print()

    return resultados


def calcular_medias(resultados):
    medias = {}

    for item in resultados:
        chave = (item["tipo_vetor"], item["tamanho"], item["algoritmo"])
        medias.setdefault(chave, []).append(item["tempo_ms"])

    return {
        chave: sum(tempos) / len(tempos)
        for chave, tempos in medias.items()
    }


def salvar_resultados_csv(resultados, caminho=RESULTADOS_CSV):
    with caminho.open("w", newline="", encoding="utf-8") as arquivo:
        campos = ["tipo_vetor", "tamanho", "algoritmo", "execucao", "tempo_ms"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(resultados)


def gerar_graficos(resultados, tamanhos=None):
    os.environ.setdefault("MPLCONFIGDIR", ".matplotlib_cache")
    import matplotlib.pyplot as plt

    tamanhos = tamanhos or TAMANHOS
    medias = calcular_medias(resultados)
    tipos = sorted({item["tipo_vetor"] for item in resultados})
    algoritmos = ["Bubble Sort", "Heap Sort"]

    for tipo in tipos:
        plt.figure(figsize=(8, 5))

        for algoritmo in algoritmos:
            valores = [
                medias[(tipo, tamanho, algoritmo)]
                for tamanho in tamanhos
            ]
            plt.plot(tamanhos, valores, marker="o", label=algoritmo)

        plt.title(f"Desempenho - Vetor {tipo}")
        plt.xlabel("Tamanho do vetor (n)")
        plt.ylabel("Tempo medio (ms)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        nome_arquivo = f"grafico_{tipo.lower()}.png"
        plt.savefig(nome_arquivo, dpi=150)
        plt.close()


def imprimir_tabela_medias(resultados, tamanhos=None):
    tamanhos = tamanhos or TAMANHOS
    medias = calcular_medias(resultados)
    tipos = sorted({item["tipo_vetor"] for item in resultados})

    print("=== MEDIAS FINAIS (ms) ===")
    print("| Tipo | n | Bubble Sort | Heap Sort |")
    print("|---|---:|---:|---:|")

    for tipo in tipos:
        for tamanho in tamanhos:
            bubble = medias[(tipo, tamanho, "Bubble Sort")]
            heap = medias[(tipo, tamanho, "Heap Sort")]
            print(f"| {tipo} | {tamanho} | {bubble:.3f} | {heap:.3f} |")


def main():
    resultados = executar_experimentos()
    salvar_resultados_csv(resultados)
    gerar_graficos(resultados)
    imprimir_tabela_medias(resultados)
    print(f"\nResultados salvos em: {RESULTADOS_CSV}")
    print("Graficos salvos em: grafico_aleatorio.png, grafico_inverso.png, grafico_ordenado.png")


if __name__ == "__main__":
    main()
