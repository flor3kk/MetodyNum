# schemat hornera - dzielenie wielomianu przez dwumian
def dziel(wielomian, dwumian):
    iloraz = []
    reszta = list(wielomian)
    while len(reszta) >= len(dwumian):
        leading_term = reszta[0] / dwumian[0]
        iloraz.append(leading_term)
        for i in range(len(dwumian)):
            reszta[i] -= leading_term * dwumian[i]
        reszta.pop(0)
    return iloraz, reszta


# uzycie
stopien = int(input("podaj stopien wielomianu: "))
wielomian = [0] * (stopien + 1)
for i in range(0, stopien):
    wielomian[i] = int(input("podaj wspolczynniki wielomianu od najwyzszego: "))

wielomian[stopien] = int(input("podaj wyraz wolny: "))

print("wielomian: ", end='')
for i in range(len(wielomian) - 1):
    print(str(wielomian[i]) + "x^" + str(stopien - i) + " + ", end='')
print(str(wielomian[stopien]))

wolny = int(input("podaj dzielnik"))
dwumian = [1, -wolny]  # dwumian x +- liczba
print("dwumian: ", end='')
print(str(dwumian[0]) + "x +" + str(dwumian[1]))
iloraz, reszta = dziel(wielomian, dwumian)

print("Dzielenie wielomianu przez dwumian schemat hornera")
print("iloraz:", iloraz)
print("reszta:", reszta)
