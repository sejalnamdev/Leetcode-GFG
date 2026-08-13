n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

answer = []
left = 0

for i in range(len(nums)):
    if i == 0:
        right = sum(nums) - nums[i]
    else:
        left += nums[i-1]
        right = sum(nums) - left - nums[i]

    absdiff = abs(left - right)
    answer.append(absdiff)

print(answer)