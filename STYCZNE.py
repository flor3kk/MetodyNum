# METODA STYCZNYCH

import sympy as sp

x = sp.symbols('x')

def funkcja(x):
    return sp.sin(x) - 0.5 * x


def prim(x1):
    return sp.diff(funkcja(x), x).subs(x, x1)


def prim2(x1):
    return sp.diff(funkcja(x), x, x).subs(x, x1)


def styczne(a, b, E):
    if funkcja(a) * funkcja(b) < 0:
        if prim2(x) != 0:
            if funkcja(a) * prim2(a) > 0:
                x0 = a
            else:
                x0 = b

            i = 0
            xn = x0 - funkcja(x0) / prim(x0)

            while abs(funkcja(xn)) > E:
                xn = xn - funkcja(xn) / prim(xn)
                i += 1

        print("szukany pierwsiatek: " + str(sp.N(xn)))
        print("liczba wszystkich iteracji: " + str(i))


if __name__ == '__main__':
    a = sp.pi / 2
    b = sp.pi
    E = 0.01

    styczne(a,b, E)


# METODA STYCZNYCH
# import math
#
# import sympy as sp
#
# x = sp.Symbol('x')
#
#
# def funkcja(x):
#     return sp.sin(x) - 0.5 * x
#
# def fprim(x1):
#     return sp.diff(funkcja(x), x).subs(x, x1)
#
# def fprim2(x1):
#     return sp.diff(funkcja(x), x, x).subs(x, x1)
#
#
# def cauchy(a, b):
#     if funkcja(a) * funkcja(b) < 0:
#         return True
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     E = 0.01
#     c = math.pi  # losowa wartość większa od E
#     a = math.pi/2
#     b = math.pi
#
#     if funkcja(a) * fprim2(a) > 0:
#         exit(1)
#     elif funkcja(b) * fprim2(b) > 0:
#         exit(1)
#
#     i = 0  # obroty
#     while abs(c) > E and cauchy(a, b):
#
#         i = i + 1
#         x = b - (funkcja(b) / fprim(b))
#         c = funkcja(x)
#
#         print("lewy przedzial: ", a, "\t\t prawy przedzial: ", b, "\t\tx: ", x, "\tf(x) = ", c, " ---- ITERACJE: ", i)
#         print(x)
#         if cauchy(a, x):
#             b = x
#         elif cauchy(x, b):
#             a = x
#         else:
#             print("Koniec możliwości, żegnam")
#
#
