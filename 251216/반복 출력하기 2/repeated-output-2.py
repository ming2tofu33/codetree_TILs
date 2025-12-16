n = int(input())

# Please write your code here.

def greet(n):
    if n == 0:
        return

    greet(n - 1)
    print("HelloWorld")

greet(n)