import sympy as sp


def f(x):
    return sp.sqrt(1 + x)
    # return 2000 * sp.log(140000 / (140000 - 2100 * x)) - 9.8 * x


def trapez(a, b, n):
    h = (b - a) / n
    print('h = ', h)

    pole = f(a) + f(b)  # PRZYPIDANIE OD RAZU FUKNCJI NA KRANCACH PRZEDZIALOW

    i = 1
    while i < n:
        pole += 2 * f(a + i * h)  # DOPISANIE DO POLA WARTOSCI PO SKOKACH
        i += 1

    return sp.N((b - a) / (2 * n) * pole)


if __name__ == '__main__':
    # AGH    print(trapez(8, 30, 2))
    print(trapez(0, 1, 3))  # DOLNY PRZEDZIAL, GORNY PRZEDZIAL, ILOSC TRAPEZOW