# Bubble Heap Sort

Projeto da disciplina de Projeto e Análise de Algoritmos para implementação e análise experimental dos algoritmos **Bubble Sort** e **Heap Sort**.

## Conteúdo

- `codigo.py`: implementação dos algoritmos, execução dos experimentos, geração do CSV e dos gráficos.
- `test_codigo.py`: testes de corretude dos algoritmos.
- `TRABALHO.md`: relatório final em Markdown.
- `resultados.csv`: resultados brutos das execuções.
- `grafico_aleatorio.png`, `grafico_inverso.png`, `grafico_ordenado.png`: gráficos gerados pelo experimento.

O notebook `analise_ordenacao.ipynb` foi mantido como material auxiliar/histórico. A fonte principal e atualizada do experimento é `codigo.py`.

## Metodologia

O experimento compara os algoritmos em três tipos de entrada:

- vetores aleatórios;
- vetores ordenados;
- vetores inversamente ordenados.

Foram usados vetores com `1000`, `3000` e `5000` elementos. Cada cenário foi executado 5 vezes e analisado pela média do tempo de execução em milissegundos.

## Como Executar

Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute os testes:

```bash
python -m unittest -v
```

Execute o experimento:

```bash
python codigo.py
```

Ao final, o script gera:

- `resultados.csv`;
- `grafico_aleatorio.png`;
- `grafico_inverso.png`;
- `grafico_ordenado.png`.

## Resultado Resumido

O Heap Sort foi mais rápido nos vetores aleatórios e inversos, como esperado para um algoritmo `O(n log n)`. O Bubble Sort foi mais rápido nos vetores já ordenados porque a implementação possui parada antecipada, ficando em `O(n)` nesse caso.
