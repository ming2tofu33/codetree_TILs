n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

max_cnt = 1

for i in range(n):
    if i == 0 or arr[i] != arr[i - 1]:
        cur_num = arr[i]
        cnt = 1
    else:
        if cur_num == arr[i]:
            cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

print(max_cnt)