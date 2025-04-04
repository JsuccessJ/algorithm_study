def KMP(A, P):
    n,m = len(A),len(P)
    pi = [0] * m
    preprocessing(P, pi, m)
    i = j = count = 0
    fail = 1
    while i < n:
        count += 1
        if j==0 or A[i]==P[j]:
            i += 1
            j += 1
        else: j = pi[j-1]
        if j == m:
            fail = 0
            j = pi[j-1]
            print(count)
    if fail: print('fail')

def preprocessing(P, pi, m):
    k = 0
    for j in range(1, m):
        while k>0 and P[k]!=P[j]: k = pi[k-1]
        if P[k]==P[j]: k += 1
        pi[j] = k

P = input()
A = input()
KMP(P, A)
