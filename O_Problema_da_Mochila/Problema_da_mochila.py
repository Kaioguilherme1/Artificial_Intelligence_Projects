# auth kaio Guilherme

from Genetics import Genetic

#       Peso, Valor
items = [[3, 266], [13, 442], [10, 671], [9, 526], [7, 388],
         [1, 245], [8, 210], [8, 145], [2, 126], [9, 322]]
MAX_WEIGHT = 35


def print_bag(chromosome: list, fitness: int):
    """
    Imprime as informações do cromossomo e seu valor de aptidão.

    Args:
        chromosome (list): Lista representando o cromossomo contendo a quantidade de cada item.
        fitness (int): Valor de aptidão do cromossomo.

    Returns:
        None
    """
    global items
    chromosome_size = len(chromosome)
    peso = 0
    valor = 0
    # adiciona o peso e o valor do item sendo o indice do gene o item é o gene a quantidade
    for index in range(0, chromosome_size):
        if chromosome[index] > 0:
            peso += chromosome[index] * items[index][0]
            valor += chromosome[index] * items[index][1]

    print(f'Fitness: {fitness}')
    print('Chromossomo: \n', chromosome,)
    print("+------------+----------+----------+")
    print("| quantidade | peso (kg)| valor ($)|")
    for item in items:
        print('| {:<10} | {:<5} kg | $ {:<6} |'.format(
            chromosome[items.index(item)], item[0], item[1]))
    print("+------------+----------+----------+")
    print('| Total -->  | {:<5} kg | $ {:<6} |'.format(peso, valor))
    print("+------------+----------+----------+")


def fitness(chromosome: list):
    """
    Calcula e retorna o valor de aptidão do cromossomo.

    Args:
        chromosome (list): Lista representando o cromossomo contendo a quantidade de cada item.

    Returns:
        int: Valor de aptidão do cromossomo.
    """
    global items
    chromosome_size = len(chromosome)
    peso = 0
    valor = 0
    score = 0
    # adiciona o peso e o valor do item sendo o indice do gene o item é o gene a quantidade
    for index in range(0, chromosome_size):
        if chromosome[index] > 0:
            peso += chromosome[index] * items[index][0]
            valor += chromosome[index] * items[index][1]

    if peso > MAX_WEIGHT:  # se o peso for maior que o peso maximo o score é negativo
        score = (MAX_WEIGHT - peso)
    else:  # se o peso for menor que o peso maximo o score é o valor - peso
        score = valor - peso

    return score

# ---------------------------- Execução ---------------------------- #

Population = Genetic(chromosome_size=len(items),
                     population_size=1000,
                     generations=50,
                     best=0.5,
                     mutation_prob=0.001,
                     fitness_function=fitness,)

results, performance = Population.run()  # executa o algoritmo genetico
Population.print_performace(performance)  # imprime o desempenho do algoritmo
# imprime o melhor resultado
print("Melhor Resultado: ")
print_bag(results[-1][2][0], results[-1][2][1])
Population.plot_graphic(results, "O_Problema_da_Mochila")
