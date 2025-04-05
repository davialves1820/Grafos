# Grafo implementação do BFS e DFS

## 📄 Descrição
Implementação da estrutura de dados grafo em python e dos algoritmos de busca em largura (BFS) e busca em profundidade (DFS).

---

## 🗂️ Arquivos
- _pycache_: Contém o arquivo executável;
- maze.py: Arquivo principal;
- grafo.py: Contém a implementação do grafo e as funções de BFS e DFS;
- ler_arquivo.py: Contém a função para ler o arquivo de entrada do grafo;
- input: Pasta que contém os arquivos .txt testes.

---

## ⚙️ Execução do código

```
python main.py
```
---

## 🖥️ Simulação

Escolha o arquivo de entrada com o tamanho do grafo.
```
Quantos vértices (4/10/50/177): 4
```
```
Matriz de adjacentes:
[0, 3, 4, 0]
[3, 0, 5, 7]
[4, 5, 0, 0]
[0, 7, 0, 0]

Vetor de adjacentes:
[1, 2]
[0, 2, 3]
[0, 1]
[1]
Busca em profundidade:
Vértice: 0
Vértice: 1
Vértice: 2
Vértice: 3
```

Escolha o vértice de origem para começar a busca em largura.
```
Digite o vértice de origem: 0
```
Escolha o vértice de destino.
```
Distância em vértices da origem até um outro vértice:
[0, 1, 1, 2]
Digite o vértice de destino: 3
```
```
Caminho da origem até o destino:
[3, 1, 0]
```
