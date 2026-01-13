n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def is_subarray(n1, n2, a, b):
    start, idx = 0, 0
    result = False

    while True:
        if start not in range(n1) or idx not in range(n2):
            break

        if result and a[start + idx] != b[idx]:
            result = False
            break

        if a[start + idx] == b[idx]:
            idx += 1
            result = True
            print(start, idx, 'idx + 1')
        else:
            start += 1
            print(start, idx, 'start +1')
    
    return result

ans = 'Yes' if is_subarray(n1, n2, a, b) else 'No'

print(ans)
# 5 3
# 1 2 3 4 5
# 4 5 6