from sorts import *
from time import *
from matplotlib import pyplot as plt
from random import shuffle


def main():
    funcs = [bubble_sort, selection_sort, insertion_sort]
    colors = ['red', 'green', 'blue']
    labels = ['пузырек', 'выбор', 'вставка']

    for i in range(len(funcs)):
        a = []
        for n in range(100, 1001, 100):
            arr = [i for i in range(n)]
            shuffle(arr)
            s = 0
            for j in range(10):
                arr1 = arr.copy()
                t1 = time_ns()
                funcs[i](arr1)
                t2 = time_ns()
                s += (t2-t1) / 1000000
            a.append(s)
        print(a)
        plt.plot(range(100, 1001, 100), a, c=colors[i], label=labels[i])

    plt.title("Произвольный случай")
    plt.xlabel("размер массива, элементов")
    plt.ylabel("время работы, мс")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()