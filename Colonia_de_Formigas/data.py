

formigueiro = [["A", 0], ["B", 5], ["C", 4], ["D", 0], ["E", 2], ["F", 3], ["G", 0], ["H", 0], ["I", 6], ["J", 0], ["K", 3], ["L", 0], ["M", 5], ["N", 0], ["O", 2], ["P", 0], ["Q", 4], ["R", 5], ["S", 0], ["T", 2]]
tuneis = [
    [2, 3, 4, 6],       # Vértice A
    [1, 3, 5],       # Vértice B
    [1, 2, 5, 9],       # Vértice C
    [1, 6, 8, 9],    # Vértice D
    [2, 3, 9,11],    # Vértice E
    [1, 4, 7],    # Vértice F
    [6, 8],    # Vértice G
    [7, 4, 9, 10],    # Vértice H
    [5, 3, 4, 8, 10, 12],    # Vértice I
    [9, 8,13,18,19] ,   # Vértice J
    [5,12,14 ],    # Vértice K
    [11,9,16,13],    # Vértice L
    [12,10,16,17],   # Vértice M
    [11,15],    # Vértice N
    [14,16],    # Vértice O
    [15,12,13,20],    # Vértice P
    [13,18],    # Vértice Q
    [17,10],    # Vértice R
    [10],    # Vértice S
    [16]    # Vértice T
    ]
distances = {
        "A": {"B": 5, "C": 7, "D": 1, "E": 4, "F": 3, "G": 8, "H": 10, "I": 9, "J": 2, "K": 8, "L": 3, "M": 7, "N": 5, "O": 6, "P": 9, "Q": 10, "R": 11, "S": 8, "T": 7},
        "B": {"A": 5, "C": 8, "E": 6},
        "C": {"A": 7, "B": 8, "E": 4, "I": 9},
        "D": {"A": 1, "E": 8, "G": 7, "H": 3},
        "E": {"A": 4, "B": 6, "C": 4, "D": 8},
        "F": {"A": 3, "E": 10, "G": 5},
        "G": {"A": 8, "D": 7, "F": 5},
        "H": {"D": 3, "G": 9, "I": 6, "P": 5},
        "I": {"A": 9, "C": 9, "H": 6, "J": 4, "P": 8},
        "J": {"I": 4, "H": 2, "K": 5, "L": 6, "Q": 9},
        "K": {"J": 5, "Q": 4, "M": 9},
        "L": {"J": 6, "M": 7, "P": 3},
        "M": {"K": 9, "L": 7, "N": 6, "P": 9},
        "N": {"M": 6, "P": 7},
        "O": {"P": 4, "Q": 8},
        "P": {"H": 5, "I": 8, "L": 3, "M": 9, "N": 7, "O": 4},
        "Q": {"J": 9, "K": 4, "O": 8, "R": 5},
        "R": {"Q": 5, "S": 3},
        "S": {"R": 3},
        "T": {"P": 7}
    }

print(distances[formigueiro[1- 1][0]][formigueiro[4 - 1][0]])