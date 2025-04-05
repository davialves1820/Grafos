from ler_arquivo import load_from

def main():

    # Solicita ao usuário o número de vértices e carrega o grafo correspondente
    n = input("Quantos vértices (4/10/50/177): ")
    grafo = load_from("input/pcv" + n + ".txt")

    # Exibe a estrutura do grafo
    grafo.exibir_grafo()

    # Realiza a busca em profundidade
    print("Busca em profundidade:")
    grafo.busca_em_profundidade()

    # Solicita o vértice de origem para a BFS
    origem = int(input("Digite o vértice de origem: "))
    d, p = grafo.busca_em_largura(origem)

    # Exibe as distâncias da origem até os demais vértices
    print("Distância em vértices da origem até um outro vértice:")
    print(d)

    # Solicita o vértice de destino e mostra o caminho
    destino = int(input("Digite o vértice de destino: "))
    print("Vértice antecessor no trajeto origem -> destino:")
    print(p)
    print("Caminho da origem até o destino:")
    grafo.caminho(p, destino)



# Executa a função main
main()