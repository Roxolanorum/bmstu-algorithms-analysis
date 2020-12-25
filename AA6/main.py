from tsp import *

def main():
    n = int(input("Выберите граф (1-3): "))

    inf = 99999

    map1 = [[inf, 4, 3, 6, 3],
            [4, inf, 7, 2, 1],
            [3, 7, inf, 5, 3],
            [6, 2, 5, inf, 4],
            [3, 1, 3, 4, inf]]

    map2 = [[inf, 1, 3, 5, 2],
            [1, inf, 7, 9, 8],
            [3, 7, inf, 5, 3],
            [5, 9, 5, inf, 6],
            [2, 8, 3, 6, inf]]

    map3 = [[inf, 3, 8, 6, 9],
            [3, inf, 7, 2, 1],
            [8, 7, inf, 5, 3],
            [6, 2, 5, inf, 4],
            [9, 1, 3, 4, inf]]

    maps = [map1, map2, map3]
    print("Точное решение: ", brute_force(maps[n-1]))


if __name__ == "__main__":
    main()
