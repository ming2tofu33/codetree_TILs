A = input()

# Please write your code here.

def palindrome(s):
    reversed_str = s[::-1]
    return reversed_str

print("Yes" if palindrome(A) == A else "No")