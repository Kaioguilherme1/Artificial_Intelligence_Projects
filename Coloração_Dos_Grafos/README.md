# Coloração dos grafos(N-cores)

O problema da coloração de grafos consiste em atribuir cores a vértices de um grafo de forma que vértices adjacentes não possuam a mesma cor. 
Neste projeto, será utilizado um algoritmo genético para encontrar a solução ótima ou uma solução aproximada para o problema. 
O algoritmo genético buscará otimizar a coloração do grafo através da evolução de uma população de soluções candidatas, aplicando operadores genéticos como seleção, cruzamento e mutação. 
O objetivo é encontrar a menor quantidade de cores necessárias para colorir o grafo, levando em consideração as restrições de adjacentes com cores diferentes.

## Índice

1. [🎒 O problema da mochila](#o-problema-da-mochila)
2. [⚙️ Requisitos](#requisitos)
3. [🔄 Como funciona](#como-funciona)
4. [🖥️ Uso](#uso)
5. [🧪 Testes](#testes)
6. [📝 Conclusão](#conclusão)
7. [📚 Referência](#referência)
8. [👨‍💻 Autor](#autor)

## ⚙️ Requisitos
- Python 3.x
- matplotlib


## 🔄 Como funciona

---

## 🖥️ Uso

---
### Utilizando a classe `Genetic` e seus parâmetros

A classe `Genetic` implementa um algoritmo genético para otimização de problemas de maximização. Ao utilizá-la, você precisa fornecer alguns parâmetros importantes:

1. `chromosome_size` (int): Representa o número de dimensões do espaço de busca. No contexto do problema da mochila, seria o número de itens disponíveis para serem selecionados.

2. `fitness_function` (Callable): É a função de avaliação que será utilizada para avaliar os indivíduos. Essa função é responsável por calcular o valor de aptidão de um cromossomo e deve ser definida de acordo com o problema em questão. No caso do exemplo fornecido, a função `fitness(chromosome: list)` foi definida para calcular o valor de aptidão de um cromossomo da mochila.

3. `fitness_minimize` (bool): Indica se a função de avaliação deve ser minimizada ou maximizada. Por padrão, o valor é definido como `False`, o que significa que o objetivo é maximizar a função de avaliação.

4. `population_size` (int): Define o tamanho da população a ser gerada. Quanto maior o tamanho da população, maior a diversidade genética e potencial de busca do algoritmo. No exemplo fornecido, o tamanho da população foi definido como 10.

5. `generations` (int): Determina o número de gerações que serão executadas. Cada geração representa uma iteração do algoritmo genético, onde ocorrem as etapas de seleção, cruzamento e mutação dos indivíduos.

6. `best` (float): Representa a proporção de melhores indivíduos que serão selecionados para reprodução. É um valor entre 0 e 1, onde 1 indica que todos os melhores indivíduos serão selecionados. No exemplo fornecido, o valor foi definido como 0.5, o que significa que metade dos melhores indivíduos será selecionada para reprodução.

7. `mutation_prob` (float): Define a taxa de mutação que será aplicada aos indivíduos selecionados para reprodução. É um valor entre 0 e 1, onde 0 indica nenhuma mutação e 1 indica uma alta taxa de mutação. No exemplo fornecido, o valor foi definido como 0.001, indicando uma baixa taxa de mutação.

8. `selection_prob` (float): Define A porcentagem de influência do rank na seleção do segundo pai para cruzamento. É um valor entre 0 e 1, onde 0 indica que o segundo pai será escolhido aleatoriamente e 1 indica que o segundo pai será sempre o melhor indivíduo. No exemplo fornecido, o valor foi definido como 0.5, o que significa que o segundo pai será escolhido aleatoriamente com 50% de chance de ser o melhor indivíduo.

### Executando o código e resultados

Para executar o código fornecido, você precisa instanciar a classe `Genetic` com os parâmetros desejados e chamar o método `run()` 
para iniciar o algoritmo genético. O método `run()` retornará os resultados finais.

Comando para executar o código:
```bash
python3 Coloração_Dos_Grafos/Coloracao_dos_grafos.py
```
obs - Deve ser executado Dentro da pasta do repositorio

No exemplo fornecido, os resultados são armazenados nas variáveis `results` e `performance`. O resultado final é exibido chamando o método `print_bag()` 
passando o cromossomo e o valor de aptidão do melhor indivíduo encontrado. Além disso, a função `plot_graphic()` é utilizada para gerar um gráfico da evolução do algoritmo ao longo das gerações.

Após a execução do algoritmo genético, serão exibidos os seguintes resultados:

- O melhor resultado encontrado, mostrando o cromossomo (quantidade de cada item na mochila), o valor de aptidão.

- O desempenho do algoritmo, que pode incluir informações como a média é tempo total de execução das funções.

- Um gráfico da evolução do algoritmo, mostrando como o valor de aptidão melhora ao longo das gerações.

Essas informações fornecem uma visão geral do desempenho do algoritmo genético na resolução do problema da mochila, permitindo avaliar a eficácia da abordagem utilizada.

## 🧪 Testes

---
## 📝 Conclusão

--- 
O algoritmo genético utilizado na resolução do problema da mochila 0-1 demonstrou eficácia na busca por soluções que maximizam o valor total dos itens incluídos na mochila, 
respeitando o limite de peso. A variação do tamanho da população impactou diretamente nos resultados, 
sendo observado um melhor desempenho com uma população maior. 
Esses resultados indicam o potencial do algoritmo genético como uma abordagem promissora para resolver problemas de otimização, como o da mochila.
## 📚 Referência:

---
- Documentação sobre Algoritmos Genéticos. Disponível em: [https://bioinfo.com.br/algoritmos-geneticos/](https://bioinfo.com.br/algoritmos-geneticos/)

## 👨‍💻 Autor

---
Este projeto foi desenvolvido por Kaio Guilherme como parte da disciplina de Inteligência Artificial do curso de Ciência da Computação da UFRR.


