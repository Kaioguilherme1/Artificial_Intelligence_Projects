# Autor: Kaio Guilherme
# Disciplina: Inteligência Artificial (DCC607) - 2023.1

# conexoes entres as cidades e suas distâncias
adjacency_list = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Bucharest': [('Pitesti', 101), ('Fagaras', 211), ('Giurgiu', 90), ('Urziceni', 85)],
    'Craiova': [('Pitesti', 138), ('Rimnicu Vicea', 146), ('Dobreta', 120)],
    'Dobreta': [('Craiova', 120), ('Mehadia', 75)],
    'Eforie': [('Hirsova', 86)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Giurgiu': [('Bucharest', 90)],
    'Hirsova': [('Eforie', 86), ('Urziceni', 98)],
    'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
    'Iasi': [('Neamt', 87), ('Vaslui', 92)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Neamt': [('Iasi', 87)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Pitesti': [('Bucharest', 101), ('Craiova', 138), ('Rimnicu Vicea', 97)],
    'Rimnicu Vicea': [('Craiova', 146), ('Sibiu', 80), ('Pitesti', 97)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu Vicea', 80), ('Arad', 140), ('Oradea', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    'Zerind': [('Arad', 75), ('Oradea', 71)]
}

# Distâncias em linha reta de Bucareste à todas as cidades do mapa
heuristic = {
    'Arad':          366,
    'Bucharest':     0,
    'Craiova':       160,
    'Dobreta':       242,
    'Eforie':        161,
    'Fagaras':       178,
    'Giurgiu':       77,
    'Hirsova':       151,
    'Iasi':          226,
    'Lugoj':         244,
    'Mehadia':       241,
    'Neamt':         234,
    'Oradea':        380,
    'Pitesti':       98,
    'Rimnicu Vicea': 193,
    'Sibiu':         253,
    'Timisoara':     329,
    'Urziceni':      80,
    'Vaslui':        199,
    'Zerind':        374
}


def A_star(start, goal, adjacency_list, heuristic):
    open_list = [start]
    close_list = []
    distance = {start: 0}
    parent = {start: None}

    while open_list:
        # Pega o nó com menor distância + heurística
        current_city = min(open_list, key=lambda city: distance[city] + heuristic[city])

        open_list.remove(current_city)
        close_list.append(current_city)

        # Se o nó atual for o nó objetivo, retorna o caminho
        if current_city == goal:
            path = []
            while current_city is not None:
                path.append(current_city)
                current_city = parent[current_city]
            # Retorna o caminho invertido
            return path[::-1]
        
        for neighbor, cost in adjacency_list[current_city]:
            # Se o vizinho já estiver na lista de fechados, pula para o próximo vizinho
            if neighbor not in close_list:
                # Calcula a distância do vizinho
                tentative_distance = distance[current_city] + cost
                # Se a distância for menor que a distância atual do vizinho, atualiza a distância e o pai
                if neighbor not in open_list or tentative_distance < distance.get(neighbor, float('inf')):
                    distance[neighbor] = tentative_distance
                    parent[neighbor] = current_city
                    if neighbor not in open_list:
                        open_list.append(neighbor)

    return None  # Não foi encontrado um caminho possível

print(A_star('Arad', 'Bucharest', adjacency_list, heuristic))