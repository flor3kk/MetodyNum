# calka 4, 1 (0,06x^2 + 2)

import sympy as sp


def f(x):
    return 0.06 * x ** 2 + 2


def prostokat(a, b, n):
    h = (b - a) / n
    print(h)

    pole = 0

    i = 1
    while i <= n:
        pole += f(a + i * h)
        i += 1

    return h * pole


if __name__ == '__main__':
    print(prostokat(1, 4, 100))  # DOLNA GRANICA, GORNA GRANICA, PODZIAL NA PROSTOKATY