n = int(input())
arr = list(map(int, input().split()))

def insertionSort(A, n):
    for i in range(1, n):
        newItem = A[i]
        j = i - 1
        while j >= 0 and newItem < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = newItem

insertionSort(arr, n)
print(arr)
