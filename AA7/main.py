from search import *


def main():
    n = int(input("Выберите метод (1-линейный, 2-бинарный, 3-частотный): "))

    methods = [lsearch, bsearch_wrap, fsearch_wrap]
    key = input("Введите искомое значение: ")

    a = list(open('names.txt', 'r').read().split('\n'))

    print("Результат поиска:", methods[n-1](a, key))


if __name__ == "__main__":
    main()
