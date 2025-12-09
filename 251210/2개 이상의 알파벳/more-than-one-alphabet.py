A = input()

# Please write your code here.

def is_more_twoalp(string):
    leng = len(string)
    for i in range(leng):
        if string[i] != string[0]:
            return True
    
    return False


if is_more_twoalp(A):
    print("Yes")
else:
    print("No")