from matplotlib import pyplot as plt

f = open("analysis.txt", "r")
a = list(map(float, f.readlines()))
single = [a[0]] * 6
multi1 = a[1:7]
multi2 = a[7:]

threads = [1, 2, 4, 8, 16, 32]
plt.plot(threads, single, c='red', label='Однопоточный алгоритм')
plt.plot(threads, multi1, c='green', label='Многопоточный алгоритм 1')
plt.plot(threads, multi2, c='blue', label='Многопоточный алгоритм 2')
plt.legend()
plt.xlabel("Число потоков")
plt.ylabel("Время работы, мс")
plt.xticks([1, 2, 4, 8, 16, 32], ["1", "2", "4", "8", "16", "32"])
plt.title("Сравнение однопоточного и многопоточных алгоритмов")
plt.show()
