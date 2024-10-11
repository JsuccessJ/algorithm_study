n, i = map(int, input().split())
arr = list(map(int, input().split()))

def select(A, i, p=0, r=n-1):
    if p == r : return A[p]
    q = partition(A, p, r)
    k = q-p+1
    if i < k: return select(A, i, p, q-1)
    elif i == k: return A[q]
    else: return select(A, i-k, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j]<=x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

print(select(arr, i))
