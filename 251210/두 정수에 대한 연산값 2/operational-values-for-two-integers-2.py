a, b = map(int, input().split())

# Please write your code here.

def change_number(a, b):
    if a > b:
        a *= 2
        b += 10
    else:        
        b *= 2
        a += 10

    return a, b

a, b = change_number(a, b)
print(a, b)