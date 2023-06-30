# auth kaio Guilherme

from Genetics import Genetic
import plotGraph as pg
import random


def generate_graph(num_nodes):
    graph = [[] for _ in range(num_nodes)]  # Lista de listas para representar o grafo
    neighbors = []

    for neighbor in range(num_nodes):
        for _ in range(3):
            neighbors.append(neighbor + 1)

    for node in range(num_nodes):
        num_neighbors = random.randint(2, min(3, len(neighbors)))

        for _ in range(num_neighbors):
            valid_neighbors = [n for n in neighbors if n != node + 1]

            if valid_neighbors:
                selected_neighbor = random.choice(valid_neighbors)
                graph[node].append(selected_neighbor)
                neighbors.remove(selected_neighbor)

    return graph


def fitness_function(chromosome):
    global graph_Arest
    conflicts = 0  # Variável para contar o número de conflitos
    visited = set()  # Conjunto para armazenar as combinações de cores e nós já visitados

    # Percorre cada nó do cromossomo
    for node, color in enumerate(chromosome, start=1):
        # Verifica os vizinhos do nó atual
        for neighbor in graph_Arest[node - 1]:
            # Verifica se há conflito de cores entre o nó atual e seu vizinho
            if chromosome[neighbor - 1] == color and (color, chromosome[neighbor - 1], neighbor) not in visited:
                # Incrementa o número de conflitos
                conflicts += 1
                # Adiciona a combinação de cores e nós no conjunto visited
                visited.add((color, chromosome[neighbor - 1], neighbor))
                visited.add((chromosome[neighbor - 1], color, node))

    return conflicts


# ----------------------print Results--------------------------

def printResults(results):
    print("Melhor Resultado: ")
    print("Chromosome: ", results[-1][0])
    print("Fitness: ", results[-1][1])


# ----------------------main--------------------------
#[1, 2, 3 ]
colors = ["red", "blue", "green", "yellow"]
graph_points = [str(i) for i in range(1, 40)]
graph_Arest = generate_graph(len(graph_points))

graph_Arest_easy = [[7, 6, 2],  # A
                    [1, 5, 3],  # B
                    [2, 4],  # C
                    [3, 9, 10],  # D
                    [2, 6, 9],  # E
                    [1, 5, 7],  # F
                    [1, 6, 8],  # G
                    [7, 14, 13],  # H
                    [5, 4, 13],  # I
                    [4, 11],  # J
                    [10, 12, 17],  # K
                    [11, 16, 13],  # L
                    [12, 8, 9],  # M
                    [8, 15],  # N
                    [14, 13, 16],  # O
                    [15, 12, 20],  # P
                    [11, 20, 18],  # Q
                    [17, 19],  # R
                    [18, 20],  # S
                    [16, 17, 19]  # T
                    ]

population = Genetic(chromosome_size=len(graph_points),
                     genes_number=4,
                     population_size=50,
                     generations=400,
                     fitness_function=fitness_function,
                     fitness_minimize=True,
                     num_elites=10,
                     mutation_prob=0.01,
                     )

results, performance = population.run()  # executa o algoritmo genetico
population.print_performace(performance)  # imprime o desempenho do algoritmo

graph = pg.Graph("Coloração de Grafos - melhor resultado", graph_points, graph_Arest, )

# imprime o melhor resultado
print("Melhor Resultado: ")
print("Número de gerações: ", len(results))
print("Chromosome: ", results[-1][0])
print("Fitness: ", results[-1][1])

# imprime o gráfico
population.plot_graphic(results, "Coloração de Grafos (4 Cores)")
graph.printColor(results[-1][1][0], colors, pause=True)

