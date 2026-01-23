n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here. 
#    상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

mapper = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3,
}

def is_wall(nr, nc):
    if 1 > nr or nr > n+1 or 1 > nc or nc > n+1:
        return True
    return False

d_num = mapper[d]
while t > 0:
    nr = r + dr[d_num]
    nc = c + dc[d_num]

    if is_wall(nr, nc):
        nr = r + dr[(d_num + 2) % 4]
        nc = c + dc[(d_num + 2) % 4]
        d_num = (d_num + 2) % 4
        t -= 1

    r = nr
    c = nc
    
    if t:
        t -= 1
    else:
        break

print(r, c)