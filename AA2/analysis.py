from matrices import *
from time import *
from matplotlib import pyplot as plt


def main():
    funcs = [classic_multiply, winograd, optimised_winograd]
    colors = ['red', 'green', 'blue']
    labels = ['классический', 'Винограда', 'улучш. Винограда']

    for i in range(len(funcs)):
        times = []
        for n in range(101, 502, 100):
            print(n)
            a = [[i+j for i in range(n)] for j in range(n)]
            c = [[0 for i in range(n)] for j in range(n)]
            s = 0
            for j in range(3):
                t1 = time_ns()
                funcs[i](a, a, c)
                t2 = time_ns()
                s += (t2-t1) / 1000000
            times.append(s)
        plt.plot(range(101, 502, 100), times, c=colors[i], label=labels[i])

    plt.title("Худший случай")
    plt.xlabel("количество строк и столбцов матрицы, эл.")
    plt.ylabel("время работы, мс")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()