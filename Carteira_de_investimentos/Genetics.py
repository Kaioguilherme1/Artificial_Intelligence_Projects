# auth kaio Guilherme
# version 2.0

import random
from typing import Callable
from matplotlib import pyplot as plt
import time


class Genetic:
    def __init__(self, chromosome_size: int,
                 genes_number: int,
                 fitness_function: Callable,
                 fitness_minimize: bool = False,
                 population_size: int = 10,
                 generations: int = 10,
                 num_elites: int = 0,
                 best: float = 0.5,
                 mutation_prob: float = 0.001,
                 selection_prob: float = 0.001):
        """
        Esta função implementa um algoritmo genético para otimização de problemas de maximização.

        Args:
            chromosome_size (int): O número de dimensões do espaço de busca.
            genes_number (int): possiveis valores que o gene pode ter a partir de 0.
            fitness_function (Callable): A função de avaliação que será utilizada para avaliar os indivíduos.
            fitness_minimize (bool): Se a função de avaliação deve ser minimizada ou maximizada.
            population_size (int): O tamanho da população a ser gerada.
            generations (int): O número de gerações que serão executadas.
            num_elites (int): O número de indivíduos que serão mantidos de uma geração para a próxima.
            best (float): A proporção de melhores indivíduos que serão selecionados para reprodução.
            mutation_prob (float): A taxa de mutação que será aplicada aos indivíduos selecionados para reprodução.
            selection_prob (float): A porcentagem de influência do rank na seleção do segundo pai.

        """
        self.chromosome_size = chromosome_size
        self.population_size = population_size
        self.genes_number = genes_number
        self.generations = generations
        self.num_elites = num_elites
        self.fitness_function = fitness_function
        self.fitness_minimize = fitness_minimize
        self.best = best
        self.mutation_prob = mutation_prob
        self.population = []
        self.results = []
        self.best_chromosome = None
        self.offsprings_list = []
        self.performace = [["crossover", 0, 0.0, 0.0],
                           ["mutation", 0, 0.0, 0.0],
                           ["selection", 0, 0.0, 0.0],
                           ["Cruzamento", 0, 0.0, 0.0],
                           0]

        probabilities = [selection_prob] + [selection_prob * (1 - i / ((population_size * best) - 1)) for i in
                                            range(1, int(population_size * best))]

        self.probabilities = probabilities


    @staticmethod
    def plot_graphic(results: list, title: str):
        geration = []
        bests_alltime = []
        bests_generation = []
        for result in results:
            geration.append(result[0])
            bests_alltime.append(result[2][1])
            bests_generation.append(result[1][1])

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(geration, bests_generation, color='red', label='Melhor fitness por geração')
        ax.plot(geration, bests_alltime, color='blue', label='Melhor fitness de todas as gerações')
        ax.set_xlabel('Geração')
        ax.set_ylabel('Melhor fitness')
        ax.set_title(title)
        ax.grid(True)
        ax.legend()

        plt.show()

    @staticmethod
    def print_performace(performance: list):
        print("+-------------+--------------+-----------------+----------------+")
        print("| função      | N° execuções | tempo Média(s)  | Tempo total(s) |")
        print("+-------------+--------------+-----------------+----------------+")
        print("| {:<12}| {:<13}| {:.8f}      | {:.4f} S       |".format(performance[0][0], performance[0][1],
                                                                        performance[0][2], performance[0][3]))
        print("| {:<12}| {:<13}| {:.8f}      | {:.4f} S       |".format(performance[1][0], performance[1][1],
                                                                        performance[1][2], performance[1][3]))
        print("| {:<12}| {:<13}| {:.8f}      | {:.4f} S       |".format(performance[2][0], performance[2][1],
                                                                        performance[2][2], performance[2][3]))
        print("| {:<12}| {:<13}| {:.8f}      | {:.4f} S       |".format(performance[3][0], performance[3][1],
                                                                        performance[3][2], performance[3][3]))
        print("+-------------+--------------+-----------------+----------------+")
        print("| Tempo total de execução: {:.4f} S                             |".format(performance[4]))
        print("+---------------------------------------------------------------+")

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
                chromosome.append(random.randint(0, self.genes_number - 1))
            population.append(chromosome)
        return population

    def crossover(self, parent1: list, parent2: list, num_offspring: int = 1) -> list:
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
        stat = time.perf_counter()
        offspring = []

        for i in range(num_offspring):
            crossover_point = random.randint(0, len(parent1) - 1)  # seleciona um ponto de crossover aleatoriamente
            child = parent1[:crossover_point] + parent2[crossover_point:]  # combina os genes dos pais
            offspring.append(child)

        end = time.perf_counter()
        self.performace[0][1] += 1  # quantidade
        self.performace[0][3] += (end - stat)  # tempo
        return offspring

    def mutation(self, chromosome: list):
        """
        Mutações aleatórias em um cromossomo
        :param chromosome:
        :return:
        """
        stat = time.perf_counter()
        for i in range(len(chromosome)):
            if random.random() < self.mutation_prob:
                chromosome[i] = random.randint(0, self.genes_number - 1)
        end = time.perf_counter()
        self.performace[1][1] += 1  # quantidade
        self.performace[1][3] += (end - stat)  # tempo
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
        stat = time.perf_counter()
        if self.fitness_minimize:
            selected = sorted(population, key=self.fitness_function)[:int(len(population) * best)]
        else:
            selected = sorted(population, key=self.fitness_function, reverse=True)[:int(len(population) * best)]
        end = time.perf_counter()
        self.performace[2][1] += 1  # quantidade
        self.performace[2][3] += (end - stat)  # tempo
        return selected

    def _elitism(self, population: list, new_population: list) -> list:
        """
        Aplica o elitismo para selecionar os melhores indivíduos das populações antiga e nova com base no numero de elites que vão permancer.

        Args:
            population (list): População antiga.
            new_population (list): Nova população.

        Returns:
            list: Nova população com os melhores indivíduos selecionados num_elites.

        """
        if self.num_elites > 0:
            best_list = population[:self.num_elites] + new_population[:self.num_elites]
            selected = self._selection(best_list, 0.5)
            new_population[:self.num_elites] = selected
        return new_population

    def _cruzamento(self, population: list, num_offspring: int = 2, best: float = 1) -> list:
        """
        Realiza o cruzamento entre os indivíduos da população.
        :param population: elementos da população
        :param num_offspring: numero de filhos a serem gerados
        :param best: proporção de indivíduos a serem selecionados
        :return:
        """
        start = time.perf_counter()
        new_population = []
        population = self._selection(population, best)  # seleciona pelo metodo de ranking
        # Seleção dos pais para cruzamento
        for parent1 in population:
            parent2 = random.choices(population, weights=self.probabilities)[0]  # seleciona pelo metodo de roleta Viciada a partir do ranking

            # Reprodução
            offspring = self.crossover(parent1, parent2, num_offspring)

            # Mutação e adição dos filhos à nova população
            for child in offspring:
                mutated_child = self.mutation(child)
                new_population.append(mutated_child)

        end = time.perf_counter()
        self.performace[3][1] += 1  # quantidade
        self.performace[3][3] += (end - start)  # tempo
        return new_population

    def run(self) -> list:
        """
            Executa o algoritmo genético.

            :return: Uma lista contendo os resultados das gerações e informações de desempenho.
                A lista contém os seguintes elementos:
                    * results: Uma lista com informações das gerações. Cada elemento é uma lista com:
                        - O número da geração.
                        - O cromossomo atualmente mais apto e sua avaliação de aptidão.
                        - O melhor cromossomo encontrado até o momento e sua avaliação de aptidão.
                    - performance: Uma lista com informações de desempenho do algoritmo genético. Contém:
                        - performace_crossover: Nome , quantidade de vezes, tempo de execução medio, tempo total
                        - performace_mutation: Nome , quantidade de vezes, tempo de execução medio, tempo total
                        - performace_selection: Nome , quantidade de vezes, tempo de execução medio, tempo total
                        - performace_cruzamento: Nome , quantidade de vezes, tempo de execução medio, tempo total
            """
        stat = time.perf_counter()
        population = self._generate_population()
        best_chromosome = population[0]
        num_offspring = int(self.population_size // (self.population_size * self.best))
        results = []
        for generation in range(self.generations):

            new_population = self._cruzamento(population, num_offspring, self.best)

            # Seleção dos indivíduos mais aptos da nova população
            new_population = self._selection(new_population, 1)

            # Avaliação do melhor cromossomo da nova população
            current_best_chromosome = new_population[0]

            # Atualização do melhor cromossomo encontrado
            if self.fitness_minimize:
                if self.fitness_function(current_best_chromosome) < self.fitness_function(best_chromosome):
                    best_chromosome = current_best_chromosome
            else:
                if self.fitness_function(current_best_chromosome) > self.fitness_function(best_chromosome):
                    best_chromosome = current_best_chromosome

            # Aplicação do elitismo
            new_population = self._elitism(population, new_population)

            # Adição dos resultados da geração atual à lista de resultados
            results.append([
                generation,
                [current_best_chromosome, self.fitness_function(current_best_chromosome)],
                [best_chromosome, self.fitness_function(best_chromosome)]
            ])

            # Atualização da população
            population = new_population
        end = time.perf_counter()
        # Calculo de desempenho
        self.performace[0][2] = self.performace[0][3] / self.performace[0][1]
        self.performace[1][2] = self.performace[1][3] / self.performace[1][1]
        self.performace[2][2] = self.performace[2][3] / self.performace[2][1]
        self.performace[3][2] = self.performace[3][3] / self.performace[3][1]
        self.performace[4] = (end - stat)
        self.results = results
        return [results, self.performace]

