from math import ceil
n, idx = map(int, input().split())
arr = list(map(int, input().split()))

def linearSelect(A,i,p=0,r=n-1):
    if r-p < 5: return select(A, i, p, r);
    t = ceil((r-p+1)/5)
    v = (r-p+1)%5
    B = [0] * t
    for j in range(0, t-1*(v!=0)):
        B[j]=select(A, 3, 5*j+p, 5*j+p+4)
    if v:
        B[-1] = select(A, ceil(v/2), 5*(t-1)+p, 5*t+v+p-6)
    M = linearSelect(B, ceil(t/2), 0, t - 1)
    q = partitionByMedian(A, p, r, M)
    k = q-p+1
    if i < k: return linearSelect(A, i, p, q-1)
    elif i == k: return A[q]
    else: return linearSelect(A, i-k, q+1, r)

def select(A, i, p, r):
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

def partitionByMedian(A, p, r, M):
    for j in range(p, r):
        if A[j]==M:
            A[j], A[r] = A[r], A[j]
            break
    return partition(A, p, r)

linearSelect(arr, idx)
