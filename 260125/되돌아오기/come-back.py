N = int(input())
moves = [tuple(input().split()) for _ in range(N)]

# Please write your code here.
#      N, S, W, E
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

mapper = {
    'N': 0,
    'S': 1,
    'W': 2,
    'E': 3
}

origin = (0, 0)
r, c, time = 0, 0, 0

def stop_moving():
    global r, c, time
    for i in range(dist):
        r += dr[mapper[dir]]
        c += dc[mapper[dir]]
        time += 1
        # print(r, c, time)
        if (r, c) == origin:
            return True
    return False

for dir, dist in moves:
    dist = int(dist)
    if stop_moving():
        break

print(time if (r, c) == origin else -1)