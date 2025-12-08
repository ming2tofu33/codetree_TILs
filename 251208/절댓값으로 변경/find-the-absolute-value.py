n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def absolute(arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] = -arr[i]

absolute(arr)

for j in arr:
    print(j, end=' ')