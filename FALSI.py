# METODA FALSI
import math


def funkcja(x):
    return 3 * x - math.cos(x) - 1


def licz(a, b):
    x = a - (funkcja(a) * (b - a) / (funkcja(b) - funkcja(a)))
    return x


def cauchy(a, b):
    if funkcja(a) * funkcja(b) < 0:
        return True
    else:
        return False


if __name__ == '__main__':
    a = 0.25
    b = 0.75
    E = 0.00001
    c = 1

    i = 0
    while (abs(c) > E and cauchy(a, b)):
        i += 1

        x = licz(a, b)
        c = funkcja(x)
        print("lewy przedzial: ", a, "\t\t prawy przedzial: ", b, "\t\tx: ", x, "\tf(x) = ", c," ---- ITERACJE: ", i)
        if (cauchy(a, x)):
            b = x
        elif (cauchy(x, b)):
            a = x
        else:
            print("siemano")
