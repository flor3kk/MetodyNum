#   f(x) = ax^3 + bx^2 + cx + d
import sympy as sp


x = sp.symbols('x')
a = sp.symbols('a')
b = sp.symbols('b')
c = sp.symbols('c')
d = sp.symbols('d')

def funkcja(px, py):
    n = len(px)
    sum=0
    for i in range(n):
        sum +=  (a * px[i] ** 3 + b * px[i] ** 2 + c * px[i] + d - py[i]) ** 2
    return sp.simplify(sum)

def aproksymacja(f):
    pochodna_a = sp.diff(f,a)
    pochodna_b = sp.diff(f,b)
    pochodna_c = sp.diff(f,c)
    pochodna_d = sp.diff(f,d)

    print("\n")
    print("\t",pochodna_a, "= 0")
    print("\t",pochodna_b, "= 0")
    print("\t",pochodna_c, "= 0")
    print("\t",pochodna_d, "= 0")

    pochodne = [pochodna_a, pochodna_b, pochodna_c, pochodna_d]

    rozw = sp.solve(pochodne, (a, b, c, d))
    print("rozwiązania: ", sp.simplify(rozw))

    return f"rozwiazanie: {rozw[a]}*x^3 + {rozw[b]}*x^2 + {rozw[c]}*x + {rozw[d]}"


if __name__ == '__main__':
    print("f(x) = ax^3 + bx^2 + cx + d")

    px = [0,3,6,9]
    py = [4,5,4,1]

    funkcja  = funkcja(px, py)
    print("Funkcja bazowa: ", funkcja)
    print(aproksymacja(funkcja))

