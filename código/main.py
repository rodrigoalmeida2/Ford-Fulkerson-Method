class Grafo:
    def __init__(self, grafo):
        self.grafo = grafo  # Matriz de adjacência do grafo
        self.V = len(grafo)  # Número de vértices

    def busca_aumentante(self, origem, destino, caminho, visitado):
        """ Busca um caminho aumentador usando DFS """
        visitado[origem] = True
        if origem == destino:
            return True  # Encontrou um caminho até o destino

        for v in range(self.V):
            if not visitado[v] and self.grafo[origem][v] > 0:
                caminho[v] = origem
                if self.busca_aumentante(v, destino, caminho, visitado):
                    return True

        return False  # Nenhum caminho encontrado

    def ford_fulkerson(self, origem, destino):
        """ Implementação do Algoritmo de Ford-Fulkerson """
        caminho = [-1] * self.V  # Array para armazenar o caminho
        fluxo_maximo = 0  # Fluxo total
        iteracao = 1  # Contador de iterações

        print("\n🔗 Estrutura inicial do grafo:")
        for i in range(self.V):
            for j in range(self.V):
                if self.grafo[i][j] > 0:
                    print(f"  {i} → {j} (capacidade: {self.grafo[i][j]})")

        while self.busca_aumentante(origem, destino, caminho, [False] * self.V):
            fluxo_caminho = float('Inf')
            v = destino
            # Encontra o menor fluxo disponível no caminho
            while v != origem:
                u = caminho[v]
                fluxo_caminho = min(fluxo_caminho, self.grafo[u][v])
                v = caminho[v]

            # Atualiza a rede residual
            v = destino
            while v != origem:
                u = caminho[v]
                self.grafo[u][v] -= fluxo_caminho
                self.grafo[v][u] += fluxo_caminho
                v = caminho[v]

            # Soma ao fluxo máximo
            fluxo_maximo += fluxo_caminho

            # Mostra a iteração atual e o fluxo somado
            print(f"\n🔄 Iteração {iteracao}:")
            print(f"  Caminho encontrado: {self.reconstroi_caminho(caminho, origem, destino)}")
            print(f"  Fluxo adicionado: {fluxo_caminho}")
            print(f"  Fluxo acumulado: {fluxo_maximo}")

            iteracao += 1

        print("\n🚀 Fluxo máximo encontrado:", fluxo_maximo)
        return fluxo_maximo

    def reconstroi_caminho(self, caminho, origem, destino):
        """ Reconstrói o caminho aumentador encontrado """
        path = []
        v = destino
        while v != origem:
            path.append(v)
            v = caminho[v]
        path.append(origem)
        path.reverse()
        return " → ".join(map(str, path))

# Gradfo 1:
grafo = [
    [0, 10, 10, 0],
    [0, 0, 2, 4],
    [0, 0, 0, 9],
    [0, 0, 0, 0]
]

# Grafo2
grafo1 = [
    [0, 7, 16, 0, 0],
    [0, 0, 0, 17, 5],  
    [0, 0, 0, 0, 26],
    [4, 0, 0, 0, 0],    
    [0, 0, 0, 20, 0]    
]

rede = Grafo(grafo1)
fluxo_maximo = rede.ford_fulkerson(0, 3)
