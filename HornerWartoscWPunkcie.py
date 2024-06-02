# schemat hornera - wyznaczanie wartosci wielomainu w punkcie
def licz(wspolczynnik, argument):
    wynik = 0
    for i in wspolczynnik:
        wynik = wynik * argument + i
    return wynik


print("Obliczanie wartosci w punkcjie - horner")

stopien = int(input("podaj stopien wielomianu: "))
lista = [0] * (stopien + 1)

for i in range(0, stopien):
    lista[i] = int(input("podaj wspolczynniki wielomianu od najwyzszego: "))

lista[stopien] = int(input("podaj wyraz wolny: "))

print("wielomian: ", end='')
for i in range(len(lista) - 1):
    print(str(lista[i]) + "x^" + str(stopien - i) + " + ", end='')
print(str(lista[stopien]))

argument = int(input("podaj punkt: "))
print(licz(lista, argument))