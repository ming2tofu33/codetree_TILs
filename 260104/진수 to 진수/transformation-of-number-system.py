a, b = map(int, input().split())
n = list(map(int, list(input())))

# Please write your code here.

num = 0

for i in n:
    num = num * a + i

digits = []

while True:
    if num < b:
        digits.append(num)
        break
    
    digits.append(num % b)
    num //= b

for digit in digits[::-1]:
    print(digit, end='')