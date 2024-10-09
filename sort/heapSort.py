n = int(input())
arr = list(map(int, input().split()))

def buildHeap(A):
    for i in range((n - 2) // 2, -1, -1):
        percolateDown(A, i)

def percolateDown(A, k):
    child = 2 * k + 1
    right = 2 * k + 2
    if child <= n - 1:
        if right <= n - 1 and A[child] < A[right]:
            child = right
        if A[k] < A[child]:
            A[k], A[child] = A[child], A[k]
            percolateDown(A, child)

def deleteMax(A):
    global n
    max = A[0]
    A[0] = A[n - 1]
    n -= 1
    percolateDown(A, 0)
    return max

def heapSort(A):
    buildHeap(A)
    for i in range(n - 1, 0, -1):
        A[i] = deleteMax(A)

heapSort(arr)
print(arr)
