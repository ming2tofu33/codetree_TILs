n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

nums.sort()
group = []
i, j = 0, len(nums) - 1

while i < j:
    group.append(nums[i] + nums[j])
    i += 1
    j -= 1

print(max(group))