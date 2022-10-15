from numpy import array
N = int(input("give table size"))
while not 5<=N<=100:
    N = int(input("size must be between 5 and 100"))
def remplir(R,Rsize):
    for i in range(Rsize):
        R[i] = int(input(f"- T[{i+1}] -"))
        while (exist(R, i, R[i]) or chifdist(R[i])) :
            R[i] = int(input(f"- T[{i+1}] -"))
def exist(R,i, n):
    j = 0
    test = True
    while test and j!=i:
        if R[j] == n:
            test = False
        else:
            j += 1
    return not test
def chifdist(n):
    i = 0
    test = True
    while i != 10 and test:
        ch = str(i)+str(i)
        if str(n).find(ch) == -1:
            i += 1
        else :
            test = False
    return not test
def zigzag(r):
    ch = str(r)
    if int(ch[0]) > int(ch[1]):
        test = False
        for i in range(1,len(ch)-1,2):
            if len(ch)%2 == 1:
                test = int(ch[i+1]) > int(ch[i]) and int(ch[i]) < int(ch[i-1])
            elif int(ch[len(ch)-1]) < int(ch[len(ch)-2]):
                    test = int(ch[i+1]) > int(ch[i]) and int(ch[i]) < int(ch[i-1])
    else :
        test = False
        for i in range(1,len(ch)-1,2):
            if len(ch)%2 == 1:
                test = int(ch[i+1]) < int(ch[i]) and int(ch[i]) > int(ch[i-1])
            elif int(ch[len(ch)-1]) > int(ch[len(ch)-2]):
                    test = int(ch[i+1]) < int(ch[i]) and int(ch[i]) > int(ch[i-1])
    return test
T = [int] * N 
remplir(T,N)
for i in range(N):
    print(f"T[{i}] = {T[i]} , zigzag = {zigzag(T[i])}")
