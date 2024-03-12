# schemat hornera - wyznaczanie wartosci wielomainu w punkcie
def licz(wspolczynnik, argument):
    wynik = 0  # -2 #-9 #-35 GITT
    for i in wspolczynnik:
        wynik = wynik * argument + i
    return wynik


print("Obliczanie wartosci w punkcjie - horner")
print(licz([-2, 0, 1], 4))


# schemat hornera - dzielenie wielomianu przez dwumian
# ?????????????
def horner(poly, x):
    result = poly[0]
    for i in range(1, len(poly)):
        result = result * x + poly[i]
    return result


def divide(poly, binomial):
    quotient = []
    remainder = list(poly)
    while len(remainder) >= len(binomial):
        leading_term = remainder[0] / binomial[0]
        quotient.append(leading_term)
        for i in range(len(binomial)):
            remainder[i] -= leading_term * binomial[i]
        remainder.pop(0)
    return quotient, remainder


# Przykładowe użycie:
poly = [5, 0, -4, 1]  # Wielomian: 5x^3 - 4x + 1
binomial = [1, -2]  # Dwumian: x - 2
quotient, remainder = divide(poly, binomial)

print("Dzielenie wielomianu przez dwumian schemat hornera")
print("Iloraz:", quotient)
print("Reszta:", remainder)


# rozwiazywanie rownan nieliniowychc metoda bisekcji, znalezc pierwsitaek rzeczywisty rownania x3 + x - 1 = 0 w przedziale 0;1 z dokladnoscia do e = 0,01;
def f(x):
    return x ** 3 + x - 1


def bisekcja(E):
    a = 0  # lewy przedzial
    b = 1  # prawy przedzial
    while abs(b - a) > E:
        c = (a + b) / 2  # wyznaczamy srodek
        if f(c) > 0:
            b = c
        else:
            a = c
    return c


print("Metoda bisekcji roziwazywanie rownan nieliniowych")
print(bisekcja(0.001))
