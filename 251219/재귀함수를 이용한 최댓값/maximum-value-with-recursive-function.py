n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def get_max(n):
    if n == 1:
        return arr[n - 1]

    a = get_max(n - 1) 
    if a > arr[n-1]:
        return a
    else:
        return arr[n-1]
    

print(get_max(n))