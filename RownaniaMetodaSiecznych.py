def f(x, f_x):
    wynik = 0
    for i in range(len(f_x)):
        wynik += f_x[i] * x ** i
    return wynik


def x_i(a, b, f_x):
    x = b - (f(b, f_x) * (b - a) / (f(b, f_x) - f(a, f_x)))
    return x


def warunekCauchyego(a, b, f_x):
    return True if f(a, f_x) * f(b, f_x) < 0 else False


# def pochodna(f_x) :
#     fp_x = [0] * (len(f(x)) - 1)
#     for i in range(fp_x) :
#         fp_x[i] = f_x(i+1) * (i+1)
#     return fp_x


if __name__ == '__main__':
    f_x = [-3, -3, 1, 1]  # funkcja
    E = 0.0001
    c = 1  # losowa wartość większa od E
    a = 1
    b = 2

    i = 1  # obroty
    while (abs(c) > E and warunekCauchyego(a, b, f_x)):
        print(i, ":")
        i = i + 1
        x = x_i(a, b, f_x)
        print("x_p =", a, "\nx_k =", b, "\nx_i =", x)
        c = f(x, f_x)
        print("f(x_p) =", f(a, f_x))
        print("f(x_k) =", f(b, f_x))
        print("f(x_i) =", c, "\n")

        if (warunekCauchyego(a, x, f_x)):
            b = x
        elif (warunekCauchyego(x, b, f_x)):
            a = x
        else:
            print("Koniec możliwości, żegnam")
