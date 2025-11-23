n, m = map(int, input().split())

# Please write your code here.
nd = set()
md = set()

for i in range(1, n +1):
    if n % i == 0:
        nd.add(i)

for j in range(1, m +1):
    if m % j == 0:
        md.add(j)

cd = nd & md

print(max(cd))