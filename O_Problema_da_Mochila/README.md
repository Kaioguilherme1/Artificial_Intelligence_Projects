# 🎒 O problema da mochila

Este projeto é uma solução para o problema da mochila 0-1 utilizando um algoritmo genético. 
No problema da mochila, recebemos um conjunto de itens, cada um com um peso e um valor, 
e precisamos determinar a quantidade de cada item a ser incluída em uma coleção de modo que o peso total seja menor ou 
igual a um determinado limite e o valor total seja o maior possível.

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
### Algoritimo Genetico
O algoritmo genético utiliza uma população de indivíduos, onde cada indivíduo representa uma solução possível para o problema da mochila. 
Cada indivíduo é representado por um cromossomo, que contém a quantidade de cada item a ser incluído na mochila, 
assim como no exemplo anterior, para saber mais sobre o funcionamento do mesmo clique [aqui](https://github.com/Kaioguilherme1/Artificial_Intelligence_Projects/tree/main/O_problema_das_N-rainhas).

### Função Fitness(apitidão)
A função de aptidão é responsável por calcular o valor de aptidão de um cromossomo, 
levando em consideração o peso e o valor dos itens selecionados. O objetivo é maximizar o valor total dos itens sem exceder o limite de peso da mochila.

### Genes Do Cromossomo
Os genes do cromossomo representam a quantidade de cada item a ser incluído. Durante o processo de evolução, 
ocorrem as etapas de seleção, cruzamento e mutação. A seleção escolhe os indivíduos mais aptos para reprodução. 
O cruzamento combina os genes de dois indivíduos para gerar novos indivíduos. A mutação faz pequenas alterações nos genes para explorar novas soluções.

### Seleção
Ao longo das gerações, o algoritmo genético busca encontrar a combinação de genes que maximize o valor dos itens incluídos na mochila, 
respeitando o limite de peso. Com o tempo, as soluções tendem a melhorar e se aproximar da solução ótima para o problema da mochila.
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
python3 O_Problema_da_Mochila/Problema_da_mochila.py 
```
obs - Deve ser executado Dentro da pasta do repositorio

No exemplo fornecido, os resultados são armazenados nas variáveis `results` e `performance`. O resultado final é exibido chamando o método `print_bag()` 
passando o cromossomo e o valor de aptidão do melhor indivíduo encontrado. Além disso, a função `plot_graphic()` é utilizada para gerar um gráfico da evolução do algoritmo ao longo das gerações.

Após a execução do algoritmo genético, serão exibidos os seguintes resultados:

- O melhor resultado encontrado, mostrando o cromossomo (quantidade de cada item na mochila), o valor de aptidão e a quantidade total de peso e valor da mochila.

- O desempenho do algoritmo, que pode incluir informações como a média, mediana e desvio padrão dos valores de aptidão ao longo das gerações.

- Um gráfico da evolução do algoritmo, mostrando como o valor de aptidão melhora ao longo das gerações.

Essas informações fornecem uma visão geral do desempenho do algoritmo genético na resolução do problema da mochila, permitindo avaliar a eficácia da abordagem utilizada.

## 🧪 Testes
Ambos os testes foram executados com a mesma tabela de itens é o peso maximo de 35 KG, assim como os mesmos parâmetros, a fim de avaliar a performance dos dois. A tabela de itens pode ser vista abaixo:

| Item | Peso (kg) | Valor ($) |
|------|-----------|-----------|
| 1    | 3         | 266       |
| 2    | 13        | 442       |
| 3    | 10        | 671       |
| 4    | 9         | 526       |
| 5    | 7         | 388       |
| 6    | 1         | 245       |
| 7    | 8         | 210       |
| 8    | 8         | 145       |
| 9    | 2         | 126       |
| 10   | 9         | 322       |

Além disso, uma tabela com os tempos de execução foi gerada e será exibida nos testes para avaliação. 
___
### Teste 1
este teste foi executado com os seguintes parâmetros:
- **Tamanho do cromossomo:** 10
- **Tamanho da população:** 50
- **Número de gerações:** 1000
- **Best:** 0.2
- **Taxa de mutação:** 0.001

como podemos observear no trecho do codigo baixo:



#### Grafico

### Resultados

#### melhor resultado:
- **Fitness:**  2568
- Chromossomo:
 [0, 0, 0, 1, 0, 6, 1, 1, 2, 0]

| quantidade | peso (kg)| valor ($)|
|------------|----------|----------|
| 0          | 3     kg | $ 266    |
| 0          | 13    kg | $ 442    |
| 0          | 10    kg | $ 671    |
| 1          | 9     kg | $ 526    |
| 0          | 7     kg | $ 388    |
| 6          | 1     kg | $ 245    |
| 1          | 8     kg | $ 210    |
| 1          | 8     kg | $ 145    |
| 2          | 2     kg | $ 126    |
| 0          | 9     kg | $ 322    |
| Total -->  | 35    kg | $ 2603   |

#### desempenho

| função      | N° execuções | tempo Média(s)  | Tempo total(s) |
|-------------|--------------|-----------------|----------------|
| crossover   | 50000        | 0.00000177    s | 0.0884 S       |
| mutation    | 100000       | 0.00000087    s | 0.0868 S       |
| selection   | 2000         | 0.00007905    s | 0.1581 S       |
| Cruzamento  | 1000         | 0.00046339    s | 0.4634 S       |

 - **Tempo total de execução:** 0.5522 S                         

### Teste 2
obs este foi o teste que gerou o melhor resultado de todos, acredito que o fitness deste e a solução ótima.

este teste foi executado com os seguintes parâmetros:
- **Tamanho do cromossomo:** 10
- **Tamanho da população:** 5000
- **Número de gerações:** 1000
- **Best:** 0.2
- **Taxa de mutação:** 0.001

como podemos observear no trecho do codigo baixo:

### Grafico



### Resultados

#### melhor resultado:
- **Fitness:** 4424
- Chromossomo:
 [8, 0, 0, 0, 0, 9, 0, 0, 1, 0]

| quantidade | peso (kg)  | valor ($)  |
|------------|------------|------------|
| 8          | 3     kg   | $ 266      |
| 0          | 13    kg   | $ 442      |
| 0          | 10    kg   | $ 671      |
| 0          | 9     kg   | $ 526      |
| 0          | 7     kg   | $ 388      |
| 9          | 1     kg   | $ 245      |
| 0          | 8     kg   | $ 210      |
| 0          | 8     kg   | $ 145      |
| 1          | 2     kg   | $ 126      |
| 0          | 9     kg   | $ 322      |
| Total -->  | 35    kg   | $ 4459     |

#### desempenho

| função      | N° execuções | tempo Média(s)  | Tempo total(s) |
|-------------|--------------|-----------------|----------------|
| crossover   | 2500000      | 0.00000247      | 6.1758 S       |
| mutation    | 5000000      | 0.00000094      | 4.6958 S       |
| selection   | 2000         | 0.00461775      | 9.2355 S       |
| Cruzamento  | 1000         | 0.23159268      | 231.5927 S     |

- **Tempo total de execução:** 236.4915 S  

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


