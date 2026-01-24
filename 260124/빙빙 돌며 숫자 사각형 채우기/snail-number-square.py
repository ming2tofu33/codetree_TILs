n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
#    우, 하, 좌, 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
r, c, d = 0, 0, 0

def is_end(r, c):
    return 0 > r or n <= r or 0 > c or m <= c

for num in range(1, n * m + 1):
    arr[r][c] = num
    nr = r + dr[d]
    nc = c + dc[d]
    if is_end(nr, nc) or arr[nr][nc] != 0:
        d = (d + 1) % 4
        nr = r + dr[d]
        nc = c + dc[d]
    r = nr
    c = nc

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()