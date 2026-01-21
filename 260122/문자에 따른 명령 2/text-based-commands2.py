dirs = input()

# Please write your code here.
dx, dy = 0, 0
x = [0, 1, 0, -1]
y = [1, 0, -1, 0]
d = 0

for dir in dirs:
    if dir == 'F':
        dx += x[d]
        dy += y[d]
    else:
        d = (d + (1 if dir == 'R' else -1)) % 4

print(dx, dy)