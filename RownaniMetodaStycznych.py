#
# def f(x):
#     return -x ** 2 + x + 1
#
# def poch(x):
#     return -2 * x  + 1
#
# def styczne(x1, ex, ey):
#     x2 = x1
#     while True:
#         x1 = x2
#         x2 = x1 - f(x1) / poch(x1)
#         if  (abs(x2 - x1) <= ex or f(x2) <= ey):
#             break
#     return x2;
#
# przyblizenie = styczne(3, 0.0001, 0.0001)
# print(f"wartosc wynosi: {przyblizenie}")
#
# stopien = int(input("podaj stopien wielominanu: "))
# wielomian = [0] * (stopien + 1)
# for i in range(0, stopien):
#     wielomian[i] = int(input("podaj wspolczynniki wielomianu od najwyzszego: "))
# wielomian[stopien] = int(input("podaj wyraz wolny: "))
#
# print("wielomian: ")
# for i in range(len(wielomian) - 1):
#     print(str(wielomian[i]) + "x^" + str(stopien - i) + " + ", end='')
# print(str(wielomian[stopien]))
#
# # OBLICZANIE PIERWSZEJ POCHODNEJ
# lista_poch = [0] * stopien
# potega = stopien
# for i in range(0, stopien ):
#     lista_poch[i] = potega * wielomian[i]
#     potega = potega - 1
#
# print("pierwsza pochodna: ")
# for i in range(len(lista_poch)):
#     print(str(lista_poch[i]) + "x^" + str(stopien - i - 1) + " + ", end='')
#
# #OBLICZANIE DRUGIEJ POCHODNEJ
# lista_sec_poch = [0] * (stopien - 1)
# potega2 = stopien - 1
# for i in range(0, stopien - 1):
#     lista_sec_poch[i] = potega2 * lista_poch[i]
#     potega2 = potega2 - 1
#
# print()
# print("druga pochodna: ")
# for i in range(len(lista_sec_poch)):
#     print(str(lista_sec_poch[i]) + "x^" + str(stopien - i - 2) + " + ", end='')

# METODA STYCZNYCH
import math


def funkcja(x):
    return math.sin(x) - (1 / 2) * x


def fp(x):
    return math.cos(x) - 1 / 2


def x_i(b):
    x = b - (funkcja(b) / fp(b))
    return x


def warunekCauchyego(a, b):
    if funkcja(a) * funkcja(b) < 0:
        return True
    else:
        return False


if __name__ == '__main__':
    E = 0.001
    c = 1  # losowa wartość większa od E
    a = math.pi / 2
    b = math.pi

    i = 1  # obroty
    while (abs(c) > E and warunekCauchyego(a, b)):
        print(i, ":")
        i = i + 1
        x = x_i(b)
        print("a =", a, "\nb =", b, "\nx_i =", x)
        c = funkcja(x)
        print("f(x_p) =", funkcja(a))
        print("f(x_k) =", funkcja(b))
        print("f(x_i) =", c, "\n")

        if (warunekCauchyego(a, x)):
            b = x
        elif (warunekCauchyego(x, b)):
            a = x
        else:
            print("Koniec możliwości, żegnam")
