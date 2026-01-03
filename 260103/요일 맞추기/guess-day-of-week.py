m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
date = [m1, d1]
total_days = 0

while True:
    if date[0] == m2 and date[1] == d2:
        break
    
    if (m1, d1) > (m2, d2):
        date[1] -= 1
        total_days -= 1
        
        if date[1] < 1:
            date[0] -= 1
            date[1] = months[date[0]]
    
    elif (m1, d1) < (m2, d2):    
        date[1] += 1
        total_days += 1
        
        if date[1] > months[date[0]]:
            date[0] += 1
            date[1] = 1

print(day_of_week[total_days % 7])