N, T = map(int, input().split())
commands = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
#    상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
r, c = N // 2, N //2
d = 0
total = board[r][c]

def is_board(r, c):
    return 0 <= r < N and 0 <= c < N

for cmd in commands:
    if cmd == "R":
        d = (d + 1) % 4
    elif cmd == "L":
        d = (d - 1) % 4
    else:
        nr = r + dr[d]
        nc = c + dc[d]
        if not (nr == r and nc == c):
            if is_board(nr, nc):
                total += board[nr][nc]
                r = nr
                c = nc
            
print(total)