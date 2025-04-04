def rabin_karp(A, P, d=26, q=113):
    n,m = len(A),len(P)
    p = b = count = 0
    for i in range(m):
        p = mod((d*p+ord(P[i])-97), q)
        b = mod((d*b+ord(A[i])-97), q)
    h = mod(d**(m-1), q)
    for i in range(n-m+1):
        print(b,end=' ')
        if i != 0: b = mod((d*(b-h*(ord(A[i-1])-97))+(ord(A[i+m-1])-97)), q)
        if p == b:
            if P[0:m] == A[i:i+m]: count += 1
    print(count)

def mod(x, y): return (x%y+y)%y

A = input()
P = input()
rabin_karp(A, P)
