import math


def f(x):
    return 3 * x - math.cos(x) - 1


def x_i(a, b):
    x = a - (f(a) * (b - a) / (f(b) - f(a)))
    return x


def warunekCauchyego(a, b):
    return True if f(a) * f(b) < 0 else False


if __name__ == '__main__':
    E = 0.00001
    f_c = 1  # losowa wartość większa od E
    a = 0.25
    b = 0.75

    i = 1  # obroty
    while (abs(f_c) > E and warunekCauchyego(a, b)):
        print(i, ":")
        i = i + 1
        x = x_i(a, b)
        print("x_p =", a, "\nx_k =", b, "\nx_i =", x)
        f_c = f(x)
        print("f(x_p) =", f(a))
        print("f(x_k) =", f(b))
        print("f(x_i) =", f_c, "\n")

        if (warunekCauchyego(a, x)):
            b = x
        elif (warunekCauchyego(x, b)):
            a = x
        else:
            print("Koniec możliwości, żegnam")
