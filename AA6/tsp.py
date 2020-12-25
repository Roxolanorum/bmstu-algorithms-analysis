from math import factorial
from itertools import permutations

def brute_force(c):
    n = len(c)
    res = 99999
    min_path = []
    for path in permutations([i for i in range(n)]):
        s = 0
        path = list(path)
        path.append(path[0])
        for i in range(len(path)-1):
            s += c[path[i]][path[i+1]]
        if s < res:
            res = s
            min_path = path
    return min_path, res


def ant_algorithm(c):
    n = len(c)
    f = [[0 for i in range(n)] for j in range(n)]

    Q = 0
    for i in range(1, n):
        for j in range(i, n):
            Q += c[i][j] + c[j][i]
    Q /= n

    m = n
    j = [[] for _ in range(m)]

    alpha = 0.5
    beta = 0.5
