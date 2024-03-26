# METODA STYCZNYCH
import math


def funkcja(x):
    return math.sin(x) - (1 / 2) * x


def fprim(x):
    return math.cos(x) - 1 / 2

def x_i(b):
    x = b - (funkcja(b) / fprim(b))
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

    i = 0  # obroty
    while (abs(c) > E and warunekCauchyego(a, b)):

        i = i + 1
        x = x_i(b)
        c = funkcja(x)

        print("lewy przedzial: ", a, "\t\t prawy przedzial: ", b, "\t\tx: ", x, "\tf(x) = ", c," ---- ITERACJE: ", i)

        if (warunekCauchyego(a, x)):
            b = x
        elif (warunekCauchyego(x, b)):
            a = x
        else:
            print("Koniec możliwości, żegnam")