n = int(input())
name = []
height = []
weight = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.

people = []

for n, h, w in zip(name, height, weight):
    people.append((n, h, w))

people.sort(key=lambda x: (x[1], -x[2]))

for person in people:
    print(*person)