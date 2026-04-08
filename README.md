# Análise Experimental de Algoritmos de Ordenação

##  Objetivo
Este projeto tem como objetivo comparar o desempenho de dois algoritmos de ordenação com diferentes complexidades:

- Bubble Sort (O(n²))
- Heap Sort (O(n log n))

A análise é feita por meio de experimentos com diferentes tipos de entrada e tamanhos de vetores.
---
##  Metodologia
Foram realizados testes considerando:

### Tipos de vetores:
- Vetores aleatórios
- Vetores ordenados (melhor caso para Bubble Sort)
- Vetores inversamente ordenados (pior caso para Bubble Sort)

### Tamanhos dos vetores:
- 1000 elementos
- 3000 elementos
- 5000 elementos

### Execuções:
- 5 execuções para cada cenário
- Utilização da média dos tempos para análise

### Métrica:
- Tempo de execução em milissegundos (ms)

---

## Tecnologias utilizadas
- Python
- Bibliotecas:
  - random
  - time
  - matplotlib

---

##  Como executar

1. Instale as dependências:

pip install matplotlib

2. Execute o código:

python codigo.py

=> O programa irá:
   -Executar os testes automaticamente
   -Exibir os tempos no terminal
   -Gerar gráficos comparativos