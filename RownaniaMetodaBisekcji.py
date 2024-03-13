# rozwiazywanie rownan nieliniowychc metoda bisekcji, znalezc pierwsitaek rzeczywisty
# rownania x3 + x - 1 = 0 w przedziale 0;1 z dokladnoscia do e = 0,01;
def f(x):
    return -x ** 2 + x + 1


def bisekcja(E):  # E epsylon
    iteracja = 0  # ile razy wykonal sie skrpyt aby obliczyc wartosc
    a = -1  # lewy przedzial
    b = 1  # prawy przedzial
    while abs(b - a) > E:
        if f(a) * f(b) < 0:
            iteracja += 1
            c = (a + b) / 2  # wyznaczamy srodek
            if f(c) > 0:
                b = c
            else:
                a = c
        else:
            print("warunek cauchyego nie zostal spelniony")
            break

    print(f"ilosc iteracji: {iteracja}")
    return c


print("Metoda bisekcji roziwazywanie rownan nieliniowych")
print(bisekcja(float(input("podaj z jaka dokładnościa Epsylon (np 0.01)"))))  # podajemy z jaka dokladnoscia
