n, s = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
INF = float('inf')
min_len = INF
i, j = 0, 1

while j < n:
    if sum(arr[i: j]) >= s:
        min_len = min(min_len, len(arr[i: j]))
        i += 1
    else:
        j += 1

print(min_len)