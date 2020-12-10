def classic_multiply(a, b, c):
    m = len(a)
    n = len(b)
    q = len(b[0])

    for i in range(m):
        for j in range(q):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c


def winograd(a, b, c):
    m = len(a)
    n = len(b)
    q = len(b[0])

    mult_a = [0] * m
    for i in range(m):
        mult_a.append(0)
        for k in range(n//2):
            mult_a[i] += a[i][2*k] * a[i][2*k + 1]

    mult_b = [0] * q
    for i in range(q):
        for k in range(n//2):
            mult_b[i] += b[2*k][i] * b[2*k + 1][i]

    for i in range(m):
        for j in range(q):
            c[i][j] = -mult_a[i] - mult_b[j]
            for k in range(n//2):
                c[i][j] += (a[i][2*k] + b[2*k+1][j]) * (a[i][2*k+1] + b[2*k][j])
            if n % 2:
                c[i][j] += a[i][-1] * b[-1][j]
    return c


def optimised_winograd(a, b, c):
    m = len(a)
    n = len(b)
    q = len(b[0])

    mult_a = [0] * m
    for i in range(m):
        for k in range(0, n - n%2, 2):
            mult_a[i] += -a[i][k] * a[i][k + 1]

    mult_b = [0] * q
    for i in range(q):
        for k in range(0, n - n%2, 2):
            mult_b[i] += -b[k][i] * b[k + 1][i]

    for i in range(m):
        for j in range(q):
            c[i][j] = mult_a[i] + mult_b[j]
            for k in range(0, n - n%2, 2):
                c[i][j] += (a[i][k] + b[k+1][j]) * (a[i][k+1] + b[k][j])
            if n % 2:
                c[i][j] += a[i][-1] * b[-1][j]
    return c
