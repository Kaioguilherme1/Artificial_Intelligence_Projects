
import plotGraph as pg # responsavel por exbir o grafo em tempo real
import data # responsavel por fornecer os dados do grafo

class Colonia():

    def __init__(self):
        self.formigueiro = data.formigueiro
        self.tuneis = data.tuneis
        self.melhor_rota = []
        self.melhor_distancia = 0


rota = [1, 3, 2, 5, 9, 8, 10, 12, 13, 18, 19, 20, 17, 16, 11, 14, 15, 7, 4, 6]

# Exemplo de atualização da melhor rota em tempo real
melhor_rota = []  # Melhor rota inicialmente vazia

# criar o grafo
formigueiro = pg.Graph("Grafo de Formigueiro" ,data.formigueiro, data.tuneis)

# Atualizar a melhor rota a cada novo item em tempo real
for novo_item in rota:
    melhor_rota.append(novo_item)
    formigueiro.printRoute(melhor_rota)

# Exibir a última atualização da rota
formigueiro.printRoute(melhor_rota ,pause=True)
