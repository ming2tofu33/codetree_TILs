N = int(input())

# Please write your code here.

def cum_sum(n):
    if n == 1:
        return 1
    
    return cum_sum(n - 1) + n

print(cum_sum(N))