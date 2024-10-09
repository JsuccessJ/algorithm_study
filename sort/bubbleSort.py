def bubbleSort(A, n):
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
