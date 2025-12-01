n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

# Please write your code here.

def bisect_left(target):
    left, right = 0, len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            if arr[mid] == target:
                ans = mid 
            right = mid - 1 

    return ans + 1 if ans != -1 else -1

for q in query:
    print(bisect_left(q))