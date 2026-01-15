M, D = map(int, input().split())

# Please write your code here.

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def valid_date(m, d):
    if m in range(1, 13):
        if d in range(1, months[m] + 1):
            return 'Yes'
    return 'No'

print(valid_date(M, D))