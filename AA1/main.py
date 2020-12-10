from levenshtein import *

def main():
    s1 = input("Введите первую строку: ")
    s2 = input("Введите вторую строку: ")
    n = int(input("Выберите метод (1-нм, 2-р, 3-рм, 4-дл):"))
    methods = [levenshtein_matrix, levenshtein_rec_wrap, levenshtein_rec_matr_wrap, dameray_levenshtein]
    print("Расстояние между строками:", methods[n-1](s1, s2))


if __name__ == "__main__":
    main()