n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
A.insert(0,0)

def div_sub():
    global m
    if m % 2:
        m -= 1
    else:
        m //= 2
    return m

add = 0

while m >= 1:
    add += A[m]
    div_sub()

print(add)