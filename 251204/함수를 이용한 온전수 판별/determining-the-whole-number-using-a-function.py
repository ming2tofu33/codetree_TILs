a, b = map(int, input().split())

# Please write your code here.

def condition(n):
    if n % 2 == 0:
        return False
    elif str(n)[-1] == '5':
        return False
    elif n % 3 == 0 and n % 9 != 0:
        return False
    else:
        return True

cnt = 0

for i in range(a, b + 1):
    if condition(i):
        cnt += 1

print(cnt)