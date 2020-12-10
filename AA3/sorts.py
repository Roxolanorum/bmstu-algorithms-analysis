def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


def selection_sort(a):
    n = len(a)
    for i in range(n):
        m, i_m = a[i], i
        for j in range(i, n):
            if a[j] < m:
                m, i_m = a[j], j
        a[i], a[i_m] = a[i_m], a[i]
    return a


def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
    return a
