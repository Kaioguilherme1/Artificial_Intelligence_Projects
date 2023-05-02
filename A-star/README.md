# A* Algorithm

Este é um exemplo de implementação do algoritmo A* (A-Star) em Python. O algoritmo é utilizado para encontrar o caminho mais curto entre dois pontos em um grafo ponderado.

## Requisitos

Para executar o script, é necessário ter o Python 3 instalado.

## Uso

Para encontrar o caminho mais curto entre duas cidades, basta chamar a função `A_star`, passando os seguintes parâmetros:

* `start`: nome da cidade de origem
* `goal`: nome da cidade de destino
* `adjacency_list`: lista de adjacência com as conexões entre as cidades e suas respectivas distâncias
* `heuristic`: dicionário com as distâncias em linha reta de Bucareste à todas as cidades do mapa

```python
print(A_star('Arad', 'Bucharest', adjacency_list, heuristic))
```

O resultado será uma lista com o caminho mais curto entre as cidades, ou `None` caso não seja possível encontrar um caminho.

## Exemplo

Considere o mapa abaixo:

![map](https://user-images.githubusercontent.com/65198889/235563683-4ef53eed-7810-4521-8c03-732911fabbd2.jpeg)

Para encontrar o caminho mais curto entre as cidades `Arad` e `Bucharest`, basta chamar a função `A_star` passando os parâmetros adequados:

```python
print(A_star('Arad', 'Bucharest', adjacency_list, heuristic))
```

O resultado será:

```
['Arad', 'Sibiu', 'Rimnicu Vicea', 'Pitesti', 'Bucharest']
```

Ou seja, o caminho mais curto entre `Arad` e `Bucharest` é `Arad -> Sibiu -> Rimnicu Vicea -> Pitesti -> Bucharest`.

## Autor

Este projeto foi desenvolvido por Kaio Guilherme como parte da disciplina de Inteligencia artificial do curso de Ciência da Computação da UFRR.
