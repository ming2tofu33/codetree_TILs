N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

ans, cnt = 0, 0
for i in range(N):
	if i >= 1 and arr[i] * arr[i - 1] > 0:
		cnt += 1
	else:
		cnt = 1
	
	ans = max(ans, cnt)

print(ans)

# max_cnt = 1

# for i in range(N):
#     cur_num = 1 if arr[i] >= 0 else -1

#     if i == 0 or cur_num != prev_num:
#         prev_num = 1 if arr[i] >= 0 else -1
#         cnt = 1
#     else:
#         cnt += 1
    
#     max_cnt = max(cnt, max_cnt)

# print(max_cnt)