n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def change_arr(arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] = -arr[i]

change_arr(arr)

for i in arr:
    print(i, end=' ')