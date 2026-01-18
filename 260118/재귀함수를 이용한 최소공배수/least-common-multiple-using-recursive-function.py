def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_list(arr, idx):
    if idx == len(arr) - 1:
        return arr[idx]
    return lcm(arr[idx], lcm_list(arr, idx + 1))


n = int(input())
nums = list(map(int, input().split()))

print(lcm_list(nums, 0))