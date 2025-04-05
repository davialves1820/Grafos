from grafos import Grafo

def load_from(fileName):
    f = open(fileName, 'r')
    n = int(f.readline())
    
    g = Grafo(n)
    
    
    l = 0
    for line in f:
        line.strip()
        numeros = line.split("\t")
        c = 0
        for i in numeros:
            if(c == n):
                break
            g.matriz_adjacentes[l][c] = int(i)
            if int(i) != 0:
                g.vetor_adjacentes[l].append(c)
            
            c += 1
        l += 1
    
    return g



n = input("Quantos vértices (4/10/50/177): ")
grafo = load_from("input/pcv" + n + ".txt")
grafo.exibir_grafo()
grafo.busca_em_profundidade()

origem = int(input("Digite o vértice de origem: "))
d, p = grafo.busca_em_largura(origem)
print("Distância em vértices da origem até um outro vértice:")
print(d)

destino = int(input("Digite o vértice de destino: "))
print("Vértice antecessor no trajeto origem -> destino:")
print(p)
print("Caminho da origem até o destino:")
grafo.caminho(p, destino)
