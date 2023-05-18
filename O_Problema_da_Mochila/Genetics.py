from joblib import Parallel, delayed
import multiprocessing
import random
import threading
import concurrent.futures
from typing import Callable
from matplotlib import pyplot as plt


class Genetic:

    def __init__(self, chromosome_size: int, fitness_function: Callable, fitness_minimize: bool = False,
                 population_size: int = 10,
                 generations: int = 10, best=0.5, mutation_prob=0.001):
        """
        Esta função implementa um algoritmo genético para otimização de problemas de maximização.

        Args:
            chromosome_size (int): O número de dimensões do espaço de busca.
            fitness_function (Callable): A função de avaliação que será utilizada para avaliar os indivíduos.
            fitness_minimize (bool): Se a função de avaliação deve ser minimizada ou maximizada.
            population_size (int): O tamanho da população a ser gerada.
            generations (int): O número de gerações que serão executadas.
            best (float): A proporção de melhores indivíduos que serão selecionados para reprodução.
            mutation_prob (float): A taxa de mutação que será aplicada aos indivíduos selecionados para reprodução.

        """
        self.chromosome_size = chromosome_size
        self.population_size = population_size
        self.generations = generations
        self.fitness_function = fitness_function
        self.fitness_minimize = fitness_minimize
        self.best = best
        self.mutation_prob = mutation_prob
        self.population = []
        self.results = []
        self.best_chromosome = None
        self.offsprings_list = []

    @staticmethod
    def plot_graphic(results: list, title: str):
        geration = []
        bests_alltime = []
        bests_generation = []
        for result in results:
            geration.append(result[0])
            bests_alltime.append(result[2][1])
            bests_generation.append(result[1][1])

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
        ax1.plot(geration, bests_generation)
        ax1.set_xlabel('Geração')
        ax1.set_ylabel('Melhor fitness')
        ax1.set_title('Melhor fitness por geração')
        ax1.grid(True)

        ax2.plot(geration, bests_alltime)
        ax2.set_xlabel('Geração')
        ax2.set_ylabel('Melhor fitness')
        ax2.set_title('Melhor fitness de todas as gerações')
        ax2.grid(True)

        fig.suptitle(title)
        plt.show()

    def _generate_population(self):
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
        for _ in range(self.population_size):
            chromosome = []
            for _ in range(self.chromosome_size):
                chromosome.append(random.randint(0, self.chromosome_size - 1))
            population.append(chromosome)
        return population

    @staticmethod
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

    def mutation(self, chromosome: list):
        """
        Mutações aleatórias em um cromossomo
        :param chromosome:
        :return:
        """
        for i in range(len(chromosome)):
            if random.random() < self.mutation_prob:
                chromosome[i] = random.randint(0, len(chromosome) - 1)
        return chromosome

    def _selection(self, population: list, best: float) -> list:
        """
        Seleciona os indivíduos mais aptos da população.

        Argumentos:
        population -- lista de indivíduos (cada indivíduo é uma lista ou tupla)
        best -- proporção de indivíduos a serem selecionados (valor padrão: 0.5)

        Retorno:
        Retorna uma lista contendo os melhores indivíduos, ordenados pelo seu fitness (aptidão).
        A quantidade de indivíduos selecionados é determinada pela proporção definida pelo argumento `best`.
        """

        if self.fitness_minimize:
            selected = sorted(population, key=self.fitness_function)[:int(len(population) * best)]
        else:
            selected = sorted(population, key=self.fitness_function, reverse=True)[:int(len(population) * best)]
        return selected

    def _cruzamento(self, population: list, num_offspring: int = 2, best: float = 1) -> list:
        new_population = []
        # Seleção dos pais para cruzamento
        for parent1 in self._selection(population, best):
            parent2 = random.choice(population)

            # Reprodução
            offspring = self.crossover(parent1, parent2, num_offspring)

            # Mutação e adição dos filhos à nova população
            for child in offspring:
                mutated_child = self.mutation(child)
                new_population.append(mutated_child)

        return new_population

    def _cruzamento_thread(self, population: list, num_offspring: int):
        new_population = self._cruzamento(population, num_offspring)
        self.offsprings_list.append(new_population)

    def _split_list(self, list: list, n: int)-> list:
        size = len(list) // n
        remainder = len(list) % n
        result = []
        index = 0
        for _ in range(n):
            sublist_size = size + (1 if remainder > 0 else 0)
            result.append(list[index:index + sublist_size])
            index += sublist_size
            remainder -= 1
        return result

    def run_te(self, multithread: bool = False) -> list: # Tentativa de implementação paralela
        population = self._generate_population()
        best_chromosome = population[0]
        num_offspring = int(self.population_size // (self.population_size * self.best))
        results = []

        lock = threading.Lock()

        manager = multiprocessing.Manager()
        offsprings_list = manager.list()

        def process_parents(parents, num_offspring, offsprings_list):
            offsprings = self._cruzamento(parents, num_offspring)
            offsprings_list.append(offsprings)

        for generation in range(self.generations):
            new_population = []

            if multithread:
                processes = []
                num_processes = 10
                parents_list = self._split_list(population, num_processes)
                for parents in parents_list:
                    p = multiprocessing.Process(target=process_parents, args=(parents, num_offspring, offsprings_list))
                    processes.append(p)
                    p.start()

                for process in processes:
                    process.join()

                for offsprings in offsprings_list:
                    new_population.extend(offsprings)

            else:
                new_population = self._cruzamento(population, num_offspring, self.best)

            # Avaliação do melhor cromossomo da nova população
            current_best_chromosome = self._selection(new_population, 1)[0]

            # Atualização do melhor cromossomo encontrado
            if self.fitness_minimize:
                if self.fitness_function(current_best_chromosome) < self.fitness_function(best_chromosome):
                    best_chromosome = current_best_chromosome
            else:
                if self.fitness_function(current_best_chromosome) > self.fitness_function(best_chromosome):
                    best_chromosome = current_best_chromosome

            # Adição dos resultados da geração atual à lista de resultados
            results.append([
                generation,
                [current_best_chromosome, self.fitness_function(current_best_chromosome)],
                [best_chromosome, self.fitness_function(best_chromosome)]
            ])

            # Atualização da população
            population = new_population

        self.results = results
        return results

    def run(self, multithread: bool = False) -> list:
        population = self._generate_population()
        best_chromosome = population[0]
        num_offspring = int(self.population_size // (self.population_size * self.best))
        results = []

        def process_parents(parents):
            offsprings = self._cruzamento(parents, num_offspring)
            return offsprings

        for generation in range(self.generations):
            new_population = []

            if multithread:
                num_processes = 10
                parents_list = self._split_list(population, num_processes)

                offsprings_list = Parallel(n_jobs=-1)(delayed(process_parents)(parents) for parents in parents_list)

                for offsprings in offsprings_list:
                    new_population.extend(offsprings)

            else:
                new_population = self._cruzamento(population, num_offspring, self.best)

            # Avaliação do melhor cromossomo da nova população
            current_best_chromosome = self._selection(new_population, 1)[0]

            # Atualização do melhor cromossomo encontrado
            if self.fitness_minimize:
                if self.fitness_function(current_best_chromosome) < self.fitness_function(best_chromosome):
                    best_chromosome = current_best_chromosome
            else:
                if self.fitness_function(current_best_chromosome) > self.fitness_function(best_chromosome):
                    best_chromosome = current_best_chromosome

            # Adição dos resultados da geração atual à lista de resultados
            results.append([
                generation,
                [current_best_chromosome, self.fitness_function(current_best_chromosome)],
                [best_chromosome, self.fitness_function(best_chromosome)]
            ])

            # Atualização da população
            population = new_population

        self.results = results
        return results

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



pop = Genetic(chromosome_size=100, population_size=1000, fitness_minimize=True, generations=1000,
              fitness_function=fitness)
results = pop.run(multithread=False)
pop.plot_graphic(results, title="8 Queens")
