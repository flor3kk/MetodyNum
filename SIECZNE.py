# METODA SIECZNYCH
def pochodna(x, wielomian):
    wynik = 0
    for i in range(len(wielomian)):
        wynik += wielomian[i] * x ** i
    return wynik


def x_i(a, b, wielomian):
    x = b - (pochodna(b, wielomian) * (b - a) / (pochodna(b, wielomian) - pochodna(a, wielomian)))
    return x


def cauchy(a, b, wielomian):
    if pochodna(a, wielomian) * pochodna(b, wielomian) < 0:
        return True
    else:
        return False


if __name__ == "__main__":
    wielomian = [-3, -3, 1, 1]
    a = 1  # lewy kraniec
    b = 2  # prawy kraniec
    c = 1
    E = 0.0001  # epsylon

    i = 0
    while (abs(c) > E and cauchy(a, b, wielomian)):
        i += 1
        x = x_i(a, b, wielomian)
        c = pochodna(x, wielomian)
        print("lewy przedzial: ", a, "\t\t prawy przedzial: ", b, "\t\tx: ", x, "\tf(x) = ", c," ---- ITERACJE: ", i)
        if (cauchy(a, x, wielomian)):
            b = x
        elif (cauchy(x, b, wielomian)):
            a = x
        else:
            print("siemano")
