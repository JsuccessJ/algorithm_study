n = int(input())
arr = list(map(int, input().split()))

def selection_sort(A, n):
    for last in range(n-1, -1, -1):
        k = theLargest(A, last)
        arr[k], arr[last] = arr[last], arr[k]
      
def theLargest(A, last):
    largest = 0
    global count
    for i in range(1, last+1):
        if A[i] >= A[largest]:
            largest = i
            count += 1
    return largest
