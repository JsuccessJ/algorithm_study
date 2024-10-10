n = int(input())
arr = list(map(int, input().split()))

def select(A, p=0, r=n-1, i):
    if p == r : return A[p]
    q = partition(A, p, r)
    k = q-p+1
    if i<k: return select(A, p, q-1, i)
    elif i==k: return A[q]
    else: return select(A, q+1, r, i-k)

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j]<x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
