from matrices import *


def main():
    m, n = map(int, input("Введите размеры матрицы A: ").split())
    print("Введите матрицу A поэлементно")
    a = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            a[i][j] = int(input())

    n, q = map(int, input("Введите размеры матрицы B: ").split())
    print("Введите матрицу B поэлементно")
    b = [[0 for i in range(q)] for j in range(n)]
    for i in range(n):
        for j in range(q):
            b[i][j] = int(input())

    c = [[0 for i in range(len(b[0]))] for j in range(len(a))]

    n = int(input("Выберите метод (1-классический, 2-Виноград, 3-улучш. Виноград): "))

    methods = [classic_multiply, winograd, optimised_winograd]
    methods[n-1](a, b, c)
    print("Результат умножения A x B")
    for i in c:
        print(' '.join(map(str, i)))


if __name__ == "__main__":
    main()
