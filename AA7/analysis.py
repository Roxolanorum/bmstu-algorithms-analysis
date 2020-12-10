from search import *
from time import *
from matplotlib import pyplot as plt
from random import shuffle


def main():
    funcs = [lsearch, bsearch_wrap, fsearch_wrap]
    colors = ['red', 'green', 'blue']
    labels = ['линейный', 'бинарный', 'частотный']

    f = open('names.txt', 'r')
    tokens = list(f.read().split('\n'))
    array = tokens.copy()
    tokens.append("НЕСУЩЕСТВУЮЩИЙ ТОКЕН")

    # a = []
    # for n in range(100, 4001, 100):
    #     b = []
    #     for token in tokens:
    #         s = 0
    #         t1 = time_ns()
    #         for j in range(10):
    #             lsearch(array[:n], token)
    #         t2 = time_ns()
    #         s += (t2-t1) / 10000000
    #         b.append(s)
    #     a.append(1.5 * sum(b)/len(b))
    # plt.plot(range(100, 4001, 100), a, c='red', label='линейный поиск')

    a = []
    for n in range(100, 4001, 100):
        b = []
        arr = array[:n]
        arr.sort()
        for token in tokens[:n]:
            s = 0
            t1 = time_ns()
            for j in range(10):
                bsearch(arr, token, 0, n)
            t2 = time_ns()
            s += (t2-t1) / 10000000
            b.append(s)
        a.append(1.5 * sum(b)/len(b))
    plt.plot(range(100, 4001, 100), a, c='green', label='бинарный поиск')


    a = []
    for n in range(100, 4001, 100):
        b = []
        arr = array[:n]
        arr.sort()
        freq = [0] * 34
        for s in arr:
            freq[ord(s[0]) - ord('А')] += 1

        for token in tokens[:n]:
            s = 0
            t1 = time_ns()
            for j in range(10):
                l = sum(freq[:ord(token[0]) - ord('А')])
                r = l + freq[ord(token[0]) - ord('А')]
                bsearch(arr, token, l, r)
            t2 = time_ns()
            s += (t2-t1) / 10000000
            b.append(s)
        a.append(1.5 * sum(b)/len(b))
    plt.plot(range(100, 4001, 100), a, c='blue', label='частотный поиск')

    plt.title("Худшее время поиска токена")
    plt.xlabel("размер словаря, элементов")
    plt.ylabel("время поиска, мс")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()