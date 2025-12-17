n = int(input())

# Please write your code here.

def ascending(n):
    if n == 0:
        return
    
    ascending(n - 1)
    print(n, end=' ')

def descending(n):
    if n == 0:
        return
    
    print(n, end=' ')
    descending(n - 1)

ascending(n)
print()
descending(n)