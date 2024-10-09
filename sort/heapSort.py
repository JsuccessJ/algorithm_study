n = int(input())
hn = n
arr = list(map(int, input().split()))

def buildHeap(A):
    for i in range((hn-2)//2, -1, -1):
        percolateDown(A, i)

def percolateDown(A, k):
    child = 2*k+1
    right = 2*k+2
    if child<=hn-1:
        if right<=hn-1 and A[child]<A[right]:
            child = right
        if A[k]<A[child]:
            A[k], A[child] = A[child], A[k]
            percolateDown(A, child)
            
def deleteMax(A):
    global hn
    max = A[0]
    A[0] = A[hn-1]
    hn-=1
    percolateDown(A,0)
    return max

def heapSort(A):
    buildHeap(A)
    for i in range(hn-1, 0, -1):
        A[i] = deleteMax(A)
