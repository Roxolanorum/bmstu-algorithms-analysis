from levenshtein import *
from time import process_time_ns
from matplotlib import pyplot as plt


def main():
    funcs = [levenshtein_matrix, levenshtein_rec_matr_wrap, dameray_levenshtein]
    colors = ['red', 'green', 'blue', 'magenta']
    labels = ['нерекурсивный матричный', 'рекурсивный матричный', 'ДЛ нерекурсивный матричный']
    for i in range(len(funcs)):
        a = []
        for l in range(0, 301, 5):
            s = 0
            for j in range(5):
                s1 = 'a' * l
                s2 = 'b' * l
                t1 = process_time_ns()
                funcs[i](s1, s2)
                t2 = process_time_ns()
                s += (t2-t1) / 1000000
            a.append(s/5)
            print(l)
        plt.plot(range(0, 301, 5), a, c=colors[i], label=labels[i])

    a = []
    for l in range(9):
        s = 0
        for j in range(5):
            s1 = 'a' * l
            s2 = 'b' * l
            t1 = process_time_ns()
            levenshtein_rec_wrap(s1, s2)
            t2 = process_time_ns()
            s += (t2-t1) / 1000000
        a.append(s / 5)

    plt.plot(range(9), a, c='magenta', label='рекурсивный нематричный')
    plt.title("Зависимость времени работы от длины строки")
    plt.xlabel("длина строки, симв.")
    plt.ylabel("время работы, мс")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()