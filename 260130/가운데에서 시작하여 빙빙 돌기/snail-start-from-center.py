n = int(input())
grid = [[0] * n for _ in range(n)]

# 시작: 정중앙
r = c = n // 2
val = 1
grid[r][c] = val

# 방향: 오른쪽, 위, 왼쪽, 아래
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

step = 1  # 이동 길이

while val < n * n:
    for d in range(4):
        for _ in range(step):
            if val == n * n:
                break
            r += dr[d]
            c += dc[d]
            val += 1
            grid[r][c] = val

        # 두 방향(오른쪽+위 / 왼쪽+아래) 끝날 때마다 step 증가
        if d % 2 == 1:
            step += 1

for row in grid:
    print(*row)