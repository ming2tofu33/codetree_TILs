N, M = map(int, input().split())
mat = [[0] * M for _ in range(N)]

# Please write your code here.
#    하, 우, 상, 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
r, c, d = 0, 0, 0

def is_end(x, y):
    return 0 > x or N <= x or 0 > y or M <= y
        
for num in range(1, N*M + 1):
    mat[r][c] = num
    nr = r + dr[d]
    nc = c + dc[d]
    if is_end(nr, nc) or mat[nr][nc] != 0:
        d = (d + 1) % 4
        nr = r + dr[d]
        nc = c + dc[d]
    r = nr
    c = nc

for i in range(N):
    for j in range(M):
        print(mat[i][j], end=' ')
    print()