commands = input()

# Please write your code here.

#    상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y, d, time, = 0, 0, 0, 0
origin = (0, 0)

for c in commands:
    if c == 'F':
        x += dx[d]
        y += dy[d]
        time += 1
        if (x, y) == origin:
            break
    elif c == 'R':
        d = (d + 1) % 4
        time += 1
    elif c == 'L':
        d = (d - 1) % 4
        time += 1

print(time if (x, y) == origin else -1)