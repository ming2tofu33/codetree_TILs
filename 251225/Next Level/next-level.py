user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.

class User:
    def __init__(self, user_id='codetree', level=10):
        self.user_id = user_id
        self.level = level
    
    def __str__(self):
        return f'user {self.user_id} lv {self.level}'

user1 = User()
print(user1)
user2 = User()
user2.user_id = user2_id
user2.level = user2_level
print(user2)