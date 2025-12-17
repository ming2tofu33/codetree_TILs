N = int(input())

# Please write your code here.

def asc_dsc(n):
    if n == 0:
        return
    
    print(n, end=' ')
    asc_dsc(n - 1)
    print(n, end=' ')

asc_dsc(N)