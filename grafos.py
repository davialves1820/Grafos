import queue

class Grafo:
    
    def __init__(self, num_vertices):
        """ Inicia as variáveis """

        self.num_vertices = num_vertices
        self.matriz_adjacentes = [[0] * num_vertices for _ in range(num_vertices)] # Cria uma matriz quadrada n com 0 em todas as posições 
        self.vetor_adjacentes = {i: [] for i in range(num_vertices)} # Cria um vetor de lista

    def exibir_grafo(self):
        """ Exibe as informações do grafo """

        print("Matriz de adjacentes:")
        for i in range(0, self.num_vertices):
            print(self.matriz_adjacentes[i])

        print()

        print("Vetor de adjacentes:") 
        for i in range(0, self.num_vertices):
            print(self.vetor_adjacentes[i])

    def busca_em_largura(self, source):
        """ Busca em largura (BFS) """

        explorados = [False] * self.num_vertices # Vetor para marcar quais vértices já foram explorados

        distancia = [-1] * self.num_vertices  # Vetor para armazenar a distância do vértice 'source' até cada outro vértice

        predecessor = [-1] * self.num_vertices  # Vetor para armazenar o predecessor de cada vértice na busca

        explorados[source] = True # Marca o vértice inicial como explorado

        fila = queue.Queue() # Fila usada para armazenar os vértices que serão visitados
        fila.put(source)
        distancia[source] = 0

        # Enquanto houver vértices na fila
        while not fila.empty():
            v = fila.get()  # Remove o primeiro vértice da fila

            for a in self.vetor_adjacentes[v]:
                
                # Se não foi explorado
                if not explorados[a]:
                    fila.put(a)  # Adiciona o vizinho à fila
                    explorados[a] = True  # Marca o vizinho como explorado
                    predecessor[a] = v  # Define o vértice atual como predecessor do vizinho
                    distancia[a] = distancia[v] + 1  # Calcula a distância do vizinho a partir da origem

        # Retorna os vetores com as distâncias e os predecessores de todos os vértices
        return distancia, predecessor

    def caminho(self, p, d):
        """ Exibe o trajeto até  o vértice d """
        # p é o vetor de antecessores dos vértices 
        
        visitados = [] # Vetor para guardar os vétices já visitados
        
        # Enquanto não chegar no destino
        while p[d] != -1:

            visitados.append(d) # Adiciona o vértice na pilha
            d = p[d] # Passa para o vértice antecessor de d

        if visitados == []:
            print("não há caminho entre os vértices")
        else:  
            visitados.append(d) # Adiciona o vértice final na pilha
            print(visitados) # Exibe o trajeto

    def busca_em_profundidade(self):
        """ Busca em profundidade (DFS) """

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
