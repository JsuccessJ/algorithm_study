n = int(input())
arr = list(map(int, input().split()))

def mergeSort(A, p=0, r=n-1):
    if p<r:
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global count
    i,j,tmp = p,q+1,[]
    while i<=q and j<=r:
        if A[i]<=A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
        count += 1
    while i<=q:
        tmp.append(A[i])
        i += 1

    while j<=r:
        tmp.append(A[j])
        j += 1
    A[p:r+1] = tmp
