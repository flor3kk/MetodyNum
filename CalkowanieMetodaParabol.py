# calka 1, -3 sin(x) * e^-3x + x^3 I BLAD MAKSYMALNY
import sympy as sp


def f(x):
    return sp.sin(x) * sp.E ** (-3 * x) + x ** 3


def parabola(a, b, n):
    h = (b - a) / n
    print("h = ", h)
    pole = 0
    pole_t = 0

    i = 1
    while i <= n:
        x = a + i * h
        pole_t += f(x - h / 2)
        if i < n:
            pole += f(x)
            i += 1
        else:
            i += 1

    pole += h / 6 * (f(a) + f(b) + 2 * pole + 4 * pole_t)

    print(pole)


if __name__ == "__main__":
    parabola(-3, 1, 6)