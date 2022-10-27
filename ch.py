from numpy import array

n = int(input("give A size"))
s = int(input("give B size"))
A = array([int] * n)
B = array([int] * s)


def remplir(T, num):
    for i in range(num):
        T[i] = int(input(f"give T[{i}]"))
        while not T[i] >= 0:
            T[i] = int(input(f"give T[{i}]"))


remplir(A, n)
remplir(B, s)


def exi(A, n, B, s):
    global pos
    test = False
    c = 0
    i = 0
    while not test and i != n:
        test = B[c] == A[i]
        i += 1
    if test:
        m = i
        while test and c != s - 1:
            c += 1
            test = B[c] == A[i]
            i += 1
    pos = m + c
    return test


print(A, B)
h = exi(A, n, B, s)
if h:
    print(f"B stops in {pos}")
