# auth kaio Guilherme

import random
import matplotlib.pyplot as plt

def Print_result(chromosome: list):  # desenha o tabuleiro com as rainhas posicionadas
    print("   ", end="")
    for i in range(len(chromosome)):
        print(" {}  ".format(i), end="")
    print("\n", end="")
    for i in range(len(chromosome)):
        print("   ", end="")
        for j in range(len(chromosome)):
            print("----", end="")
        print("\n", end="")
        print("{} |".format(i), end="")
        for j in range(len(chromosome)):
            if chromosome[i] == j:
                print(" R |", end="")
            else:
                print("   |", end="")
        print("\n", end="")
    print("   ", end="")
    for j in range(len(chromosome)):
        print("----", end="")
    print("\n", end="")

def plot_generations(results):
    """
    Plota um gráfico com os resultados de cada geração.
    :param results: lista de resultados gerados pelo algoritmo genético.
    :return:
    """
    geration = []
    bests_alltime = []
    bests_generation = []
    for result in results:
        geration.append(result[0])
        bests_alltime.append(result[2][1])
        bests_generation.append(result[1][1])

    # cria a figura com dois subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))

    # plota o primeiro gráfico no primeiro subplot
    ax1.plot(geration, bests_generation)
    ax1.set_xlabel('Geração')
    ax1.set_ylabel('Melhor fitness')
    ax1.set_title('Melhor fitness por geração')
    ax1.grid(True)

    # plota o segundo gráfico no segundo subplot
    ax2.plot(geration, bests_alltime)
    ax2.set_xlabel('Geração')
    ax2.set_ylabel('Melhor fitness')
    ax2.set_title('Melhor fitness de todas as gerações')
    ax2.grid(True)

    # exibe a figura com os dois subplots
    plt.show()


def crossover(parent1: list, parent2: list, num_offspring: int = 1) -> list:
    """
    Realiza o crossover entre dois pais para gerar um ou mais filhos.

    Argumentos:
    parent1 -- primeiro pai, uma lista representando um cromossomo.
    parent2 -- segundo pai, uma lista representando um cromossomo.
    num_offspring -- o número de filhos a serem gerados (valor padrão: 1).

    Retorno:
    Retorna uma lista contendo um ou mais filhos gerados pelo crossover.
    Cada filho é uma lista representando um cromossomo que é resultado da combinação dos pais.
    O número de filhos gerados é determinado pelo argumento `num_offspring`.
    O ponto de crossover é selecionado aleatoriamente entre os pais.
    """
    offspring = []

    for i in range(num_offspring):
        crossover_point = random.randint(0, len(parent1) - 1)  # seleciona um ponto de crossover aleatoriamente
        child = parent1[:crossover_point] + parent2[crossover_point:]  # combina os genes dos pais
        offspring.append(child)

    return offspring


def mutation(chromosome: list, mutation_prob: float = 0.001):
    """
    Mutações aleatórias em um cromossomo
    :param chromosome:
    :param mutation_prob:
    :return:
    """
    for i in range(len(chromosome)):
        if random.random() < mutation_prob:
            chromosome[i] = random.randint(0, len(chromosome) - 1)
    return chromosome


def fitness(chromosome: list):
    """
    Retorna o numero de colições que ocorreram entre as rainhas
    :param chromosome:
    :return:
    """
    # retorna o número de pares de rainhas que se atacam, logo quanto menor o valor, melhor
    underscore = 0
    length = len(chromosome)
    for i in range(0, length - 1):
        for j in range(i + 1,
                       length):  # alterei o range para evitar contar a colisão de uma rainha com ela mesma e remover
            # duplicidades
            if chromosome[i] == chromosome[j]:
                underscore += 1

            # print(chromosome[i], chromosome[j], i, j)
            if abs(chromosome[i] - chromosome[j]) == abs(i - j):
                underscore += 1

    return underscore


def Generate_population(chromosome_size: int, population_size: int):
    """
        Gera uma população inicial de indivíduos para um algoritmo genético.

        Argumentos:
        chromosome_size -- o número máximo de valores que cada gene do cromossomo pode ter.
        population_size -- o tamanho da população a ser gerada.

        Retorno:
        Retorna uma lista de indivíduos, onde cada indivíduo é uma lista de genes (cromossomo).
        O valor de cada gene é um número inteiro aleatório entre 0 e chromosome_size - 1.
        O tamanho da população é determinado pelo argumento `population_size`.
    """
    population = []
    for _ in range(population_size):
        chromosome = []
        for _ in range(chromosome_size):
            chromosome.append(random.randint(0, chromosome_size - 1))
        population.append(chromosome)
    return population


def selection(population: list, best: float = 0.5) -> list:
    """
    Seleciona os indivíduos mais aptos da população.

    Argumentos:
    population -- lista de indivíduos (cada indivíduo é uma lista ou tupla)
    best -- proporção de indivíduos a serem selecionados (valor padrão: 0.5)

    Retorno:
    Retorna uma lista contendo os melhores indivíduos, ordenados pelo seu fitness (aptidão).
    A quantidade de indivíduos selecionados é determinada pela proporção definida pelo argumento `best`.
    """

    pop_sorted = sorted(population, key=lambda x: fitness(x))  # ordena a população pelo fitness
    selected = pop_sorted[:int(len(pop_sorted) * best)]  # seleciona os melhores indivíduos
    return selected


def Genetic_N_QUEENS(dimensions=8, population_size=10, generations=100, best=0.5, mutation_rate=0.001):
    """
    Esta função implementa um algoritmo genético para otimização de problemas de maximização.

    Args:
        dimensions (int): O número de dimensões do espaço de busca.
        population_size (int): O tamanho da população a ser gerada.
        generations (int): O número de gerações que serão executadas.
        best (float): A proporção de melhores indivíduos que serão selecionados para reprodução.
        mutation_rate (float): A taxa de mutação que será aplicada aos indivíduos selecionados para reprodução.

    Returns: list: Uma lista de resultados contendo a geração atual, o melhor indivíduo da geração atual e o melhor
    indivíduo encontrado até o momento.

    """
    population = Generate_population(dimensions, population_size)
    best_chromosome = population[0]
    num_offspring = int(
        population_size // (population_size * best))  # define o número de filhos que serão gerados por geração
    results = []

    for generation in range(generations):
        new_population = []

        # Seleção dos pais
        for parent1 in selection(population, best):
            parent2 = random.choice(population)

            # Reprodução
            offspring = crossover(parent1, parent2, num_offspring)

            # Mutação e adição dos filhos à nova população
            for child in offspring:
                mutated_child = mutation(child, mutation_rate)
                new_population.append(mutated_child)

        # Avaliação do melhor cromossomo da nova população
        current_best_chromosome = selection(new_population, 1)[0]

        # Atualização do melhor cromossomo encontrado
        if fitness(current_best_chromosome) < fitness(best_chromosome):
            best_chromosome = current_best_chromosome

        # Adição dos resultados da geração atual à lista de resultados
        results.append([generation,
                        [current_best_chromosome, fitness(current_best_chromosome)],
                        [best_chromosome, fitness(best_chromosome)]])

        # Atualização da população
        population = new_population

    return results


results = Genetic_N_QUEENS(dimensions=8, population_size=100, generations=100)

for result in results:
    print(f"Geração: {result[0]} | melhor dessa geração: {result[1][1]} | melhor até agora: {result[2][1]}")

print("Melhor resultado encontrado: ")
print(f"Geração: {results[-1][0]} | Genótipo: {results[-1][2][0]} | fitness: {results[-1][2][1]}")
Print_result(results[-1][2][0])  # mostra o melhor resultado encontrado

plot_generations(results)