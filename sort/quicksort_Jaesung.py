def quick_sort(arr, start, end):
  if start >= end:
    return
  pivot = start
  left = start + 1
  right = end
  
  while left <= right:
    # left, right 멈출 때 까지 아래 두 while문 실행
    while left <= end and arr[left] <= arr[pivot]:
      left += 1
    
    while right > start and arr[right] >= arr[pivot]:
      right -= 1

    # 멈추면 아래 코드 시작
    if left > right: # 엇갈린 경우는 피벗교체
      arr[pivot], arr[right] = arr[right], arr[pivot]
    else: # 엇갈린 건 아니면 단순교체
      arr[left], arr[right] = arr[right], arr[left]
    
      # 왼쪽, 오른쪽 다시 정렬
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


# 메모리 좀 더 쓰는 코드, 좀 더 쉬움
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
