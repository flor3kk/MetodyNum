import numpy as np

def eliminacja_guassa(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)

    for i in range(n):
        max_row = np.argmax(abs(A[i:n, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x

A = np.array(   [[3, 0, 6],
                        [1, 2, 8],
                        [4, 5, -2]])

b = np.array([-12, -12, 39])

x = eliminacja_guassa(A, b)
print("Rozwiązanie x:", x)
