import sympy as sp

x = sp.symbols('x')


def lagrange(px, py):
    n = len(px)
    sum = 0
    for i in range(n):
        m1 = py[i]
        m2 = 1
        for j in range(n):
            if j != i:
                m1 *= (x - px[j])
                m2 *= (px[i] - px[j])
        sum += m1 / m2
    return sp.simplify(sum)


def newton_interpolation(px, py):

    def divided_diff(px, py):
        n = len(px)
        tab = [y for y in py]
        for j in range(1, n):
            for i in range(n - 1, j - 1, -1):
                tab[i] = (tab[i] - tab[i - 1]) / (px[i] - px[i - j])
        return tab

    tab = divided_diff(px, py)
    n = len(tab)
    N = tab[0]
    for i in range(1, n):
        term = tab[i]
        for j in range(i):
            term *= (x - px[j])
        N += term
    return sp.simplify(N)


if __name__ == '__main__':
    px = [1, 2, 3]
    py = [5, 7, 6]

    print("lagrange ", lagrange(px, py))

    print("newton ", newton_interpolation(px, py))
