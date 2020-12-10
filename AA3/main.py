from sorts import *


def main():
    a = list(map(int, input("Введите массив: ").split()))
    n = int(input("Выберите метод (1-пузырек, 2-выбор, 3-вставка): "))

    methods = [bubble_sort, selection_sort, insertion_sort]
    methods[n-1](a)
    print("Отсортированный массив:", ' '.join(map(str, a)))


if __name__ == "__main__":
    main()
