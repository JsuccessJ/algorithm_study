n = int(input())
arr = list(map(int, input().split()))

def selectionSort(A, n):
    for last in range(n - 1, -1, -1):
        k = theLargest(A, last)
        arr[k], arr[last] = arr[last], arr[k]

def theLargest(A, last):
    largest = 0
    for i in range(1, last + 1):
        if A[i] >= A[largest]:
            largest = i
    return largest

selectionSort(arr, n)
print(arr)
