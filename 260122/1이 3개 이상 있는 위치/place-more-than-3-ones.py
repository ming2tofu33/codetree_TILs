n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
r, c = 0, 0
ans = 0

for row in grid:
    cnt = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
            print(grid[nr][nc], nr, nc)
            cnt += 1
    if cnt >= 3:
        ans += 1

print(ans)