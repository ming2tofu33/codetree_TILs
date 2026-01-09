N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

max_cnt = 1

for i in range(N):
    cur_num = 1 if arr[i] >= 0 else -1

    if i == 0 or cur_num != prev_num:
        prev_num = 1 if arr[i] >= 0 else -1
        cnt = 1
    else:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

print(max_cnt)        