n = int(input())

OFFSET = 100
MAX_R = 200

line = [0] * (MAX_R + 1)
loc = OFFSET + 1

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'L':
        for i in range(loc - 1, loc - x - 1, -1):
            line[i] += 1
        loc -= x
    else:
        for i in range(loc, loc + x):
            line[i] += 1
        loc += x

# print(line)
# print(list(filter(lambda a: a >= 2, line)))
f = list(filter(lambda a: a >= 2, line))
print(len(f))