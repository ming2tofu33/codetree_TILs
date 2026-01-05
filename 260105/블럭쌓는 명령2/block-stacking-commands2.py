n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

blocks = [0] * (n+1)

for cmd in commands:
    a, b = cmd
    for i in range(a, b+1):
        blocks[i] += 1

print(max(blocks))