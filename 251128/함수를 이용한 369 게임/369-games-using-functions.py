a, b = map(int, input().split())

# Please write your code here.

def game369(x, y):
    cnt = 0

    for i in range(x, y + 1):
        tmp = list(str(i))
        if i % 3 == 0:
            cnt += 1
        elif '3' in tmp or '6' in tmp or '9' in tmp:
            cnt += 1
        
    return cnt

print(game369(a, b))