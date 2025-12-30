n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.

people = [(n, h, w) for n, h, w in zip(name, height, weight)]

people.sort(key=lambda x: x[0])
print('name')
for person in people:
    print(*person)
print()

print('height')
people.sort(key=lambda x: -x[1])
for person in people:
    print(*person)