n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# U, R, D, L
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
mapper = {'U': 0, 'R': 1, 'D': 2, 'L': 3}

d = mapper[d]

def is_wall(x, y):
    return x < 1 or x > n or y < 1 or y > n

for _ in range(t):
    nr, nc = r + dr[d], c + dc[d]
    if is_wall(nr, nc):
        d = (d + 2) % 4   # 방향만 반대로 (시간 1초 소비, 위치 그대로)
    else:
        r, c = nr, nc     # 한 칸 이동

print(r, c)