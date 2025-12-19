n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def get_max(a):
    if a == 0:
        return arr[0]

    return max(get_max(a-1), arr[a])

print(get_max(n-1))