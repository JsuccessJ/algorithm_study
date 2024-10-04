n = int(input())
hn = n
arr = list(map(int, input().split()))
count = 0

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

def bubble_sort(A, n):
    global count
    for i in range(n-1, 0, -1):
        swap = True
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swap = True
                count += 1
        if not swap:
            break


def insertion_sort(A, n):
    global count
    for i in range(1, n):
        newItem = A[i]
        j = i - 1
        while j >= 0 and newItem < A[j]:
            A[j + 1] = A[j]
            j -= 1
            count += 1
        A[j + 1] = newItem
        count += 1


def merge_sort(A, p=0, r=n-1):
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


def quick_sort(A, p, r):
    if p<r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def partition(A, p, r):
    global count
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j]<x:
            i += 1
            A[i], A[j] = A[j], A[i]
            count += 1
    A[i+1], A[r] = A[r], A[i+1]
    count += 1
    return i+1


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

def heap_sort(A):
    buildHeap(A)
    for i in range(hn-1, 0, -1):
        A[i] = deleteMax(A)

def shell_sort(A, n):
    h = n//2
    while h>3:
        for k in range(0, h):
            stepInsertionSort(A, k, h)
        h//2
a
def stepInsertionSort(A, k, h):
    for i in range(k+h, hn, h):
        newItem = A[i]
        j = i-h
        while j >= 0 and newItem < A[j]:
            A[j+h] = A[j]
            j -= h
        A[j+h] = newItem

shell_sort(arr, n)
print(arr)
