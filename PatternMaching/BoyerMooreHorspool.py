from collections import defaultdict

def BoyerMooreHorspool(A, P):
    n,m = len(A), len(P)
    match = count = 0
    jump = {P[m-1] : m}
    default_value = m
    for w in range(m-1): jump[P[w]] = m-w-1
    custom_jump = defaultdict(lambda: default_value, jump)
    i = 0
    while i < n-m+1:
        j = m-1
        k = i+m-1
        while j>=0 and P[j]==A[k]:
            count += 1
            j -= 1
            k -= 1
        if j == -1: match += 1
        i += custom_jump[A[k]]
    print(count, match)

P = input()
A = input()
BoyerMooreHorspool(P, A)
