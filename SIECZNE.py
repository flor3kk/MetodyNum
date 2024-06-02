# METODA SIECZNYCH
import sympy as sp

x_sym = sp.Symbol('x')


def f(x):
    return x ** 3 + x ** 2 - 3 * x - 3


def fprime(x):
    return sp.diff(f(x), x_sym)


def fprime2(x):
    return sp.diff(fprime(x), x_sym)


def x_i(a, b):
    x = b - (f(b) * (b - a) / (f(b) - f(a)))
    return x


def cauchy(a, b):
    if f(a) * f(b) < 0:
        return True
    else:
        return False


if __name__ == "__main__":
    a = 1  # lewy kraniec
    b = 2  # prawy kraniec
    c = 1
    E = 0.0001  # epsylon

    if fprime(a) * fprime2(a) > 0:
        exit(1)
    elif fprime(b) * fprime2(b) > 0:
        exit(1)

    i = 0
    while (abs(c) > E and cauchy(a, b)):
        i += 1
        x = x_i(a, b)
        c = f(x)
        print("lewy przedzial: ", a, "\t\t prawy przedzial: ", b, "\t\tx: ", x, "\tf(x) = ", c, " ---- ITERACJE: ", i)
        if (cauchy(a, x)):
            b = x
        elif (cauchy(x, b)):
            a = x
        else:
            print("siemano")