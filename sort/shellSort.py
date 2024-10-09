n = int(input())
arr = list(map(int, input().split()))

def shellSort(A, n):
    h = n//2
    while h:
        for i in range(h, n):
            insertionItem = A[i]
            j = i - h
            while j >= 0 and insertionItem < A[j]:
                A[j + h] = A[j]
                j -= h
            A[j + h] = insertionItem
        h //= 2

shellSort(arr, n)
print(arr)
