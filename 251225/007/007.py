secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class Code007:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time
    
    def __str__(self):
        return f'secret code : {self.code} \nmeeting point : {self.place} \ntime : {self.time}'

mission1 = Code007(secret_code, meeting_point, time)
print(mission1)