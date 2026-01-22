n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 0

for row in range(n):
    for col in range(n):
        cnt = 0
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1

print(ans)