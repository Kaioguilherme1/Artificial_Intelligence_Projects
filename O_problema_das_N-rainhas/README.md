# 👑 O problema das N rainhas
---
Este é um projeto desenvolvido para a disciplina de Inteligência Artificial do curso de Ciência da Computação da UFRR. O objetivo é solucionar o problema das oito rainhas usando algoritmos genéticos.

## Índice
1. [👑 O problema das N rainhas ](#o-problema-das-n-rainhas)
2. [⚙️ Requisitos](#requisitos)
3. [🔄 Como funciona](#-como-funciona)
4. [Esquema](#esquema)
5. [🖥️ Uso](#uso)
6. [🧪 Exemplos de teste](#exemplos-de-teste)
7. [💡 Possíveis melhorias](#possíveis-melhorias)
8. [‍💻 Autor](#autor)

## ⚙️ Requisitos
- Python 3.x
- matplotlib

## 🔄 Como funciona
Este projeto implenta um algoritmo genético para resolver o problema das N rainhas. O objetivo é encontrar um arranjo de N rainhas em um tabuleiro NxN que não se atacam (não existem duas rainhas na mesma linha, coluna ou diagonal).

O algoritmo genético é uma técnica de busca baseada na seleção natural. A ideia é iniciar com uma população aleatória de indivíduos, cada um representando uma possível solução para o problema. Esses indivíduos são então avaliados por uma 
função de fitness, que mede o quão boa é sua solução. Os indivíduos com melhor fitness têm uma maior chance de sobreviver e se reproduzir, 
combinando seus genes para criar novos indivíduos. Ao longo do tempo, a população evolui em direção a soluções cada vez melhores.

No caso desta implementação segue abaixo o esquema de funcionamento do algoritimo e a explicação de cada etapa
## Esquema

![Genetic_Diagram](https://github.com/Kaioguilherme1/Artificial_Intelligence_Projects/assets/65198889/a60f5220-9531-4b9c-809e-4bd0a08379b0)

### 1. Cromossomo: 
O cromossomo é representado por um vetor de genes (um gene é uma posição no vetor). Neste código, o vetor é criado com base em um tamanho determinado,
como por exemplo este cromossomo [1, 2, 3, 4, 5, 6, 7, 8] que representa um tabuleiro 8x8 com 8 rainhas.

### 2. Gene:
O gene é uma posição no vetor do cromossomo, que representa uma característica ou atributo do indivíduo. 
No código, os genes são criados aleatoriamente através da função `Generate_population(dimensions, population_size)`

### 3. geração: 
E o numero de gerações que os indivíduos irão se reproduzir, no código é representado pela variável `generations`

### 4. seleção:
A função de seleção neste algoritmo seleciona os indivíduos mais aptos da população, em uma proporção determinada pelo parâmetro "best". 
A população é ordenada em ordem crescente de aptidão (fitness) e os melhores indivíduos são selecionados para reprodução, 
garantindo uma boa base genética para a próxima geração.

### 4.1 fitness:
A função fitness recebe uma lista de inteiros representando a posição de cada rainha em um tabuleiro de xadrez, onde o índice da lista representa a coluna e o valor na posição representa a linha em que a rainha está.

A função utiliza um algoritmo de contagem de colisões entre as rainhas. Para cada par de rainhas, 
a função verifica se elas estão na mesma linha ou na mesma diagonal. Se as rainhas estiverem na mesma linha ou diagonal, 
incrementa uma variável underscore. O valor retornado é a quantidade total de pares de rainhas que se atacam, 
ou seja, o número de colisões entre as rainhas. Quanto menor o valor retornado, melhor é o desempenho do indivíduo na seleção natural.


### 5. Cruzamento:
A seleção dos pais é realizada na função selection. Primeiramente, a população é ordenada pelo fitness de cada indivíduo. Em seguida, é selecionada uma proporção dos melhores indivíduos, definida pelo argumento best, que serão os pais da próxima geração. Um segundo pai é escolhido aleatoriamente da população atual. Esse processo é realizado para cada pai selecionado.

### 5.1 elitismo:
O elitismo neste algoritmo consiste em selecionar o melhor cromossomo da nova população e compará-lo com o melhor cromossomo encontrado até o momento.
Se o fitness do novo cromossomo for melhor, ele é escolhido como o novo melhor cromossomo, caso contrário, o cromossomo anterior é mantido.

Ou seja, mesmo que a seleção natural (seleção de pais, reprodução e mutação) possa produzir indivíduos mais aptos, o algoritmo garante que o melhor indivíduo encontrado até o momento não seja descartado e continue presente garantindo assim que o mais apto nunca seja perdido. Isso aumenta as chances do algoritmo convergir para uma solução ótima ou próxima do ótimo.

### 5.2 crossover:
A função crossover recebe dois pais (parent1 e parent2) que são representados por listas, e um parâmetro que define quantos filhos serão gerados (num_offspring).

O objetivo dessa função é criar um ou mais filhos a partir da combinação dos genes dos pais. Para isso, é selecionado um ponto de crossover aleatório entre as duas listas que representam os pais. Esse ponto de crossover é onde os genes dos pais serão divididos, e os filhos serão gerados a partir dessa divisão.

A partir do ponto de crossover, os genes do parent1 são colocados em uma lista, e os genes do parent2 são colocados em outra lista. A partir dessas listas, são gerados os filhos, combinando os genes dos pais. O número de filhos gerados é determinado pelo parâmetro num_offspring.

Ao final, a função retorna uma lista com os filhos gerados pelo crossover.

### 5.3 mutação:
A função mutation é responsável por realizar mutações aleatórias em um cromossomo. Ela recebe um cromossomo (representado por uma lista) e uma probabilidade de mutação (valor padrão: 0.001).

A função percorre cada gene do cromossomo e verifica se deve haver uma mutação nesse gene, utilizando a probabilidade de mutação passada como argumento. Se o número gerado aleatoriamente for menor que a probabilidade de mutação, o gene é substituído por um novo valor aleatório (gerado utilizando a função random.randint()).

Essa função é importante para adicionar variação genética à população, evitando que o algoritmo genético fique preso em mínimos locais e permitindo que novas soluções sejam descobertas durante o processo de evolução


## 🖥️ Uso

Para otimizar problemas de maximização com a função Genetic_N_QUEENS, basta seguir os seguintes passos:

Chame a função Genetic_N_QUEENS, passando os seguintes parâmetros:
* `dimensions`: o número de dimensões do espaço de busca
* `population_size`: o tamanho da população a ser gerada
* `generations`: o número de gerações que serão executadas
* `best`: a proporção de melhores indivíduos que serão selecionados para reprodução
* `mutation_rate`: a taxa de mutação que será aplicada aos indivíduos selecionados para reprodução

2. A função retornará uma lista de resultados contendo a geração atual, o melhor indivíduo da geração atual e o melhor indivíduo encontrado até o momento.

O melhor indivíduo encontrado pela função Genetic_N_QUEENS será uma lista representando a posição de cada rainha no tabuleiro, de forma que duas rainhas não se ataquem. O objetivo é maximizar o número de rainhas que podem ser posicionadas no tabuleiro sem se atacarem.

## 🧪 Exemplos de teste

## Teste 1

Foi realizado o teste com 8 rainhas padrões com os seguintes parâmetros:

- Tamanho da população: 100
- Número de gerações: 10
- N° de rainhas: 8
- Taxa de mutação: 0.001
- Melhor resultado esperado: 0.5

Assim gerando estes resultados:
Melhor resultado encontrado: 
Geração: 99  
Genótipo: [5, 2, 6, 1, 6, 4, 0, 7]  
fitness: 1
### Tabuleiro
        0   1   2   3   4   5   6   7  
       --------------------------------
    0 |   |   |   |   |   | R |   |   |
       --------------------------------
    1 |   |   | R |   |   |   |   |   |
       --------------------------------
    2 |   |   |   |   |   |   | R |   |
       --------------------------------
    3 |   | R |   |   |   |   |   |   |
       --------------------------------
    4 |   |   |   |   |   |   | R |   |
       --------------------------------
    5 |   |   |   |   | R |   |   |   |
       --------------------------------
    6 | R |   |   |   |   |   |   |   |
       --------------------------------
    7 |   |   |   |   |   |   |   | R |
       --------------------------------

### Gráfico

![Teste1_grafh](https://github.com/Kaioguilherme1/Artificial_Intelligence_Projects/assets/65198889/9256b2a7-f078-4501-9c31-b22f54a74a3b)

## Teste 2

Foi realizado o teste com 50 rainhas com os seguintes parâmetros:

- Tamanho da população: 100
- Número de gerações: 4000
- N° de rainhas: 50
- Taxa de mutação: 0.001
- Melhor resultado esperado: 0.5

Assim gerando estes resultados:
Melhor resultado encontrado: 
Geração: 3999 
Genótipo: [1, 10, 28, 24, 6, 17, 37, 26, 33, 8, 3, 18, 30, 43, 4, 48, 20, 49, 40, 2, 34, 41, 45, 0, 35, 9, 31, 19, 25, 23, 47, 44, 32, 22, 12, 16, 46, 29, 7, 11, 38, 27, 5, 2, 39, 15, 42, 14, 21, 0] 
fitness: 4

### Tabuleiro

Neste caso não foi possível gerar o tabuleiro devido ao tamanho do mesmo.

### Gráfico
---
![Teste2_grafh](https://github.com/Kaioguilherme1/Artificial_Intelligence_Projects/assets/65198889/eae47e66-eda1-4dec-a55d-55adb96c8620)
---

## 💡 Possíveis melhorias
- O algoritmo poderia ser paralelizado para explorar mais eficientemente o espaço de soluções.
- 
## Autor
Este projeto foi desenvolvido por Kaio Guilherme como parte da disciplina de Inteligência Artificial do curso de Ciência da Computação da UFRR.