def find_rot_count(arr):
    low = 0
    high = len(arr) - 1
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return low
n = int(input())
arr = list(map(int,input().split()))
print(find_rot_count(arr))