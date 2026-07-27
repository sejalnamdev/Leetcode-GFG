n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

nums.sort()

a = nums[len(nums)-1]
b = nums[len(nums)-2]

print((a-1)*(b-1))