import networkx as nx
import matplotlib.pyplot as plt

class Graph():

    def __init__(self, title, vertices, arestas):
        self.title = title
        self.vertices = vertices
        self.arestas = arestas
        self.graph = self._createGraph()
        self.pos = nx.spring_layout(self.graph, k=0.2)
        self.name = nx.get_node_attributes(self.graph, 'nome')
        self.legend = nx.get_node_attributes(self.graph, 'legenda')

    def _createGraph(self):
        Graph = nx.Graph()

        # Adicionar vértices com seus nomes e legendas
        for i, (nome, legenda) in enumerate(self.vertices):
            Graph.add_node(i + 1, nome=nome, legenda=legenda)

        # Adicionar as arestas
        for i, vizinhos in enumerate(self.arestas):
            for vizinho in vizinhos:
                Graph.add_edge(i + 1, vizinho)

        return Graph

    def printRoute(self, melhor_rota=None, pause=False):

        # Definir cores dos nós
        node_color = 'lightblue'
        if melhor_rota:
            node_color = ['red' if node in melhor_rota else 'lightblue' for node in self.graph.nodes]

        plt.clf()  # Limpar a figura atual

        # Desenhar os vértices com seus nomes e legendas
        nx.draw_networkx_nodes(self.graph, self.pos, node_color=node_color, node_size=500)
        nx.draw_networkx_labels(self.graph, self.pos, labels=self.name, font_size=12, font_color='black')
        nx.draw_networkx_labels(self.graph, pos={node: (x, y - 0.13) for node, (x, y) in self.pos.items()},
                                labels=self.legend, font_size=10, font_color='darkblue', verticalalignment='top')

        # Desenhar as arestas do grafo
        nx.draw_networkx_edges(self.graph, self.pos, width=1, alpha=0.5, edge_color='gray')

        # Desenhar a melhor rota se fornecida
        if melhor_rota:
            arestas_rota = [(melhor_rota[i], melhor_rota[i + 1]) for i in range(len(melhor_rota) - 1)]
            nx.draw_networkx_edges(self.graph, self.pos, edgelist=arestas_rota, width=2, alpha=1, edge_color='red')

        # Definir título
        plt.title(self.title)

        # Definir as legendas
        red_patch = plt.Line2D([], [], color='red', marker='o', markersize=10, label='Melhor Rota')
        blue_patch = plt.Line2D([], [], color='blue', marker='o', markersize=10, linestyle='None', label='Lixo')
        plt.legend(handles=[red_patch, blue_patch])

        plt.axis('off')

        # Atualizar a exibição do gráfico
        plt.draw()
        plt.pause(0.001)  # Pausa para permitir a atualização da exibição
        # Pausar no final da execução
        if pause and melhor_rota:
            input("Pressione Enter para continuar...")
