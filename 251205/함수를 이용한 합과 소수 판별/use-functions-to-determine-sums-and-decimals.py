a, b = map(int, input().split())

# Please write your code here.

is_prime = [True] * (b + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(b ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, b + 1, i):
            is_prime[j] = False

def is_add_even(n):
    l = list(map(int,str(n)))
    if sum(l) % 2 == 0:
        return True
    return False

cnt = 0

for i in range(a, b + 1):
    if is_prime[i]:
        if is_add_even(i):
            cnt += 1

print(cnt)