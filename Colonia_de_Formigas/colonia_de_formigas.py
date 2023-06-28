import plotGraph as pg # responsavel por exbir o grafo em tempo real
import data # responsavel por fornecer os dados do grafo
import numpy as np
import random


import random

class AntColonyOptimization:
    def __init__(self, data, num_ants: int, ant_capacity: int, num_iterations: int, decay_rate: float, alpha: float, beta: float):
        self.data = data
        self.num_ants = num_ants
        self.ant_capacity = ant_capacity
        self.num_iterations = num_iterations
        self.decay_rate = decay_rate
        self.alpha = alpha
        self.beta = beta
        self.pheromone = self._init_pheromone()

    def _init_pheromone(self):
        pheromone = []
        for node_index, node in enumerate(self.data.formigueiro):
            pheromone.append([])
            for neighbor in self.data.tuneis[node[1]]:
                neighbor_index = neighbor - 1
                pheromone[node_index].append(
                    [0, 0.0])  # [quantidade de feromônio, força do feromônio entre 0 e 1, sendo 0 inexistente]
        return pheromone

    def _add_pheromone(self, edge):
        self.pheromone[edge[0]][edge[1]][0] += 1
        self.pheromone[edge[0]][edge[1]][1] = 1

    def _evaporate_pheromone(self):
        for node in self.data.formigueiro:
            for neighbor in self.data.tuneis[node[1]]:
                self.pheromone[node[0]][neighbor][1] *= self.decay_rate

    def _generate_ants(self):
        ants = []
        for i in range(self.num_ants):
            ants.append({
                'current_node': random.randint(1, len(self.data.formigueiro)),
                'visited_nodes': [],
                'distance': 0,
                'trash': 0,
                'trash_capacity': self.ant_capacity,

            })
        return ants

    def _ant_move(self, ant):
        # inicializa a lista de vizinhos do nó atual
        neighbors = []
        # lista de vizinhos do nó atual e coleta suas informações
        for neighbor in self.data.tuneis[ant['current_node']]:  # obtém os índices dos vizinhos do nó atual
            print("neibor ",neighbor)
            print("ant ",ant['visited_nodes'])

            if neighbor not in ant['visited_nodes']:
                neighbors.append({'node': neighbor,
                                  'pheromone': self.pheromone[ant['current_node'] - 1][neighbor - 1],
                                  'distance': self.data.distances[self.data.formigueiro[ant['current_node'] - 1][0]][
                                      self.data.formigueiro[neighbor['node'] - 1][0]],
                                  })


        # calcula a probabilidade de cada vizinho ser escolhido
        probabilities = []
        for neighbor in neighbors:
            probability = (neighbor['pheromone'][0] ** self.alpha) * (neighbor['pheromone'][1] ** self.alpha) * (
                        (1 / neighbor['distance']) ** self.beta)
            probabilities.append(probability)

        print(probabilities)
    def teste(self):
        ants = self._generate_ants()
        for ant in ants:
            self._ant_move(ant)


aco = AntColonyOptimization(data, num_ants=10, ant_capacity=2, num_iterations=100, decay_rate=0.5, alpha=1, beta=2)
aco.teste()

# print("Melhor rota:", best_route)
# print("Distância total:", total_distance)