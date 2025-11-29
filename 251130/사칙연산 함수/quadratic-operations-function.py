a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def operation(x, o, y):
    if o == '+':
        return f'{x} + {y} = {x + y}'
    elif o == '-':
        return f'{x} - {y} = {x - y}'
    elif o == '/':
        return f'{x} / {y} = {x / y}'
    elif o == '*':
        return f'{x} * {y} = {x * y}'
    else:
        return False

print(operation(a, o, c))