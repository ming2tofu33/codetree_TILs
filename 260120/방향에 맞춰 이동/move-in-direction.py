n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
c = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

# Please write your code here.
x, y = 0, 0

for dir, dist in moves:
    if dir == 'N':
        x += c['N'][0] * dist 
        y += c['N'][1] * dist 
    elif dir == 'S':
        x += c['S'][0] * dist 
        y += c['S'][1] * dist 
    elif dir == 'E':
        x += c['E'][0] * dist 
        y += c['E'][1] * dist 
    elif dir == 'W':
        x += c['W'][0] * dist 
        y += c['W'][1] * dist 

print(x, y)    