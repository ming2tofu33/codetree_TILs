m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

month, day = m1, d1
elapsed_days = 0

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    if month == m2 and day == d2:
        break

    elapsed_days += 1
    day += 1

    if day > months[month]:
        month += 1
        day = 1

print(elapsed_days + 1)


# def num_of_days(m, d):
#     days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     total_days = 0
    
#     for i in range(1, m):
#         total_days += days[i]
    
#     total_days += d
    
#     return total_days    

# total_days = num_of_days(m2, d2) - num_of_days(m1, d1) + 1
# print(total_days)