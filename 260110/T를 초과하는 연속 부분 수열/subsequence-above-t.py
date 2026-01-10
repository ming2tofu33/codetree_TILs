n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cnt, max_cnt = 0, 0 

for i in range(n):
    if arr[i] <= t:
        cnt = 0
    else:
        cnt += 1
        max_cnt = max(cnt, max_cnt)

print(max_cnt)