a, b = map(int, input().split())

# Please write your code here.

def contains_369(n):
    tmp = list(str(n))
    if '3' in tmp or '6' in tmp or '9' in tmp:
        return True
    else:
        return False
        
def is_369_num(n):
    return contains_369(n) or (n % 3 == 0)

cnt = 0
for i in range(a, b + 1):
    if is_369_num(i):
        cnt += 1

print(cnt)