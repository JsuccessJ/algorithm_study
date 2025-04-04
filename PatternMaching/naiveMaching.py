def naive_matching(A, P):
    n,m = len(A), len(P)
    count = compare = 0
    for i in range(n-m+1):
        match = True
        for j in range(m):
            compare += 1
            if A[i+j] != P[j]:
                match = False
                break
        if match: count += 1
    print(compare, count)

A = input()
P = input()
naive_matching(A, P)
