# auth kaio Guilherme

from Genetics import Genetic

investments = [  # ["Nome", "Tipo", "Retorno Anual", "Risco"],
    ["Petrobras", 0, 15, 20],
    ["Itaúsa", 0, 12, 10],
    ["Vale", 0, 18, 30],
    ["PetroRio", 0, 17, 25],
    ["BTG Pactual", 0, 13, 20],
    ["Braskem", 0, 16, 30],
    ["XP Long Biased", 1, 10, 15],
    ["HGLG11", 1, 8, 10],
    ["KNRI11", 1, 9, 15],
    ["HGRE11", 1, 11, 20],
    ["HFOF11", 1, 9, 20],
    ["BCFF11", 1, 8, 10],
    ["iShares S&P 500", 2, 20, 30],
    ["iShares MSCI Brazil", 2, 16, 25],
    ["Vanguard Total Stock", 2, 14, 20],
    ["iShares MSCI Emerging", 2, 18, 30],
    ["Invesco QQQ Trust", 2, 20, 30],
    ["iShares MSCI Japan", 2, 15, 20],
    ["Amazon Inc.", 3, 25, 30],
    ["Apple Inc.", 3, 22, 25],
    ["Microsoft Corporation", 3, 18, 20],
    ["Tesla Inc.", 3, 30, 35],
    ["Google LLC", 3, 24, 25],
    ["Facebook Inc.", 3, 21, 20],
    ["Tesouro Selic", 4, 4, 5],
    ["CDB", 4, 5, 5],
    ["LCI", 4, 6, 5],
    ["CDB", 4, 4, 5],
    ["LCA", 4, 5, 5],
    ["Tesouro IPCA", 4, 7, 5]
]

investments_type = ["Ações", "Fundos Imobiliários", "ETFs", "BDRs", "Renda Fixa"]


def fitness_function(chromosome) -> int:
    """
    Calcula e retorna o valor de aptidão do cromossomo.

    :param chromosome:O cromossomo representando a seleção de investimentos.
    :type chromosome: list
    :return:
    """

    global investments, investments_type
    # ----------------------pesos--------------------------
    dividend_Weight = 1
    risk_Weight = 0.5
    type_Weight = 1
    num_investments_max_Weight = 0.1
    # -----------------------------------------------------
    score = 0
    type_investments = [0, 0, 0, 0, 0]
    risks = []
    dividends_yield = []
    risk_total = 0
    dividends_yield_total = 0
    num_investments = 0

    # coleta os dados do cromossomo
    for i, gene in enumerate(chromosome):
        if gene == 1:
            num_investments += 1
            investment = investments[i]
            type_investments[investment[1]] += 1
            risks.append(investment[3])
            dividends_yield.append(investment[2])


    # calcula o score negativo com base no tipo de investimento
    for i in range(len(type_investments)):
        if type_investments[i] > 1:
            score -= 1 * type_Weight


    # # calcula o score positivo com base no risco e no retorno // opção 1
    # if len(risks) > 0:
    #     risk_total = sum(risks) / len(risks)  # calcula a média ponderada dos riscos
    # if len(dividends_yield) > 0:
    #     dividends_yield_total = sum(dividends_yield) / len(dividends_yield)
    #
    # score += dividends_yield_total * dividend_Weight
    # score -= risk_total * risk_Weight

    # opção 2
    score += sum(dividends_yield) * dividend_Weight
    score -= sum(risks) * risk_Weight


    if num_investments > num_investments_max:
        score = (num_investments_max - num_investments) * num_investments_max_Weight
    elif num_investments < num_investments_max:
        score = (num_investments - num_investments_max) * num_investments_max_Weight

    return int(score)


def print_result(chromosome, score, investments_type, investments):
    """
    Imprime o resultado da seleção de investimentos.

    :param chromosome: O cromossomo representando a seleção de investimentos.
    :type chromosome: list
    :param investments_type: Os tipos de investimentos.
    :type investments_type: list
    :param investments: Os investimentos disponíveis.
    :type investments: list
    """
    risks = []
    dividends_yield = []
    risk_total = 0
    dividends_yield_total = 0
    investiments_selected = []

    print("Chromosome: ", chromosome)
    print("Fitness: ", score)
    print("+---------------------------+----------------------+--------+--------+")
    print("| {:25s} | {:20s} | {:6s} | {:6s} |".format("Nome", "Tipo", "DiY", "Risco"))
    print("+---------------------------+----------------------+--------+--------+")
    for i, gene in enumerate(chromosome):
        if gene == 1:
            investment = investments[i]
            dividends_yield.append(investment[2])
            risks.append(investment[3])
            print("| {:25s} | {:20s} | {:5}% | {:5}% |".format(investments[i][0], investments_type[investments[i][1]],
                                                               investments[i][2], investments[i][3]))

    if len(risks) > 0:
        risk_total = sum(risks) / len(risks)  # calcula a média ponderada dos riscos
    if len(dividends_yield) > 0:
        dividends_yield_total = sum(dividends_yield) / len(dividends_yield)
    print("+---------------------------+----------------------+--------+--------+")
    print("| {:25s} | {:20s} | {:5}% | {:5}% |".format("Total", "media ponderada", int(dividends_yield_total), int(risk_total)))
    print("+---------------------------+----------------------+--------+--------+")


# ----------------------main--------------------------
num_investments_max = 30

population = Genetic(chromosome_size=len(investments),
                     genes_number=2,
                     population_size=100,
                     generations=100,
                     fitness_function=fitness_function,
                     num_elites=4,
                     )

results, performance = population.run()  # executa o algoritmo genetico
population.print_performace(performance)  # imprime o desempenho do algoritmo

# imprime o melhor resultado
print("Melhor Resultado: ")
print_result(results[-1][2][0], results[-1][2][1], investments_type, investments)
population.plot_graphic(results, "Carteira de Investimentos")
