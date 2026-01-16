Y, M, D = map(int, input().split())

# Please write your code here.

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap_year(Y):
    months[2] = 29

def is_valid_date(m, d):
    if m in range(1, 13):
        if d in range(1, months[m] + 1):
            return True
    return False

def season(m):
    if m in range(3, 6):
        return 'Spring'
    elif m in range(6, 9):
        return 'Summer'
    elif m in range(9, 12):
        return 'Fall'
    else:
        return 'Winter'

print(season(M) if is_valid_date(M, D) else -1)