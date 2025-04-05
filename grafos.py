import queue

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz_adjacentes = [[0] * num_vertices for _ in range(num_vertices)] # Cria uma matriz quadrada n com 0 em todas as posições 
        self.vetor_adjacentes = {i: [] for i in range(num_vertices)} # Cria um vetor de lista

    def exibir_grafo(self):
        print("Matriz de adjacentes:")
        for i in range(0, self.num_vertices):
            print(self.matriz_adjacentes[i])
        print()
        print("Vetor de adjacentes:") 
        for i in range(0, self.num_vertices):
            print(self.vetor_adjacentes[i])

    def busca_em_largura(self, source):
        explorados = [False] * self.num_vertices
        distancia = [-1] * self.num_vertices
        predecessor = [-1] * self.num_vertices

        explorados[source] = True

        # Fila para salvar os vértices já visitados
        fila = queue.Queue()
        fila.put(source)
        distancia[source] = 0

        while fila.empty() == False:
            v = fila.get()

            for a in self.vetor_adjacentes[v]:
                if explorados[a] == False:
                    fila.put(a)
                    explorados[a] = True
                    predecessor[a] = v
                    distancia[a] = distancia[v] + 1

        return distancia, predecessor

    def caminho(self, p, d):
        visitados = []
        
        while p[d] != -1:
            visitados.append(d)
            d = p[d]
        if visitados == []:
            print("não há caminho entre os vértices")
        else: 
            visitados.append(d)
            print(visitados)

    def busca_em_profundidade(self):
        visitados = [] # Vetor para guardar os vértices já visitados

        # Percorre todos os vértices
        for v in range(self.num_vertices):
            # Verifica se o vértice já foi visitado
            if v in visitados: 
                continue

            stack = [v] # Adiciona o vértice no topo da pilha

            # Enquanto a pilha não for vazia
            while stack:
                vertice = stack[-1] # Pega o topo da pilha

                # Se ele não tiver sido visitado exibe o vértice e adiciona no vetor visitados
                if vertice not in visitados:
                    print(f"Vértice: {vertice}")
                    visitados.append(vertice)

                free = False # Variável auxiliar para saber se encontrou algum vizinho

                # Percorre todos os vizinhos de um vértice para saber se tem algum que ainda não foi visitado
                for i in self.vetor_adjacentes[vertice]:
                    if i not in visitados:
                        stack.append(i) # Adiciona ao topo da pilha
                        free = True
                        break
                
                # Se não encotrou nenhum vizinho remove o topo da pilha
                if not free:
                    stack.pop()
