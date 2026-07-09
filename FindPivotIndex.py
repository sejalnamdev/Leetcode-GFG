class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        left = 0

        for i in range(len(nums)):
            if i > 0:
                left += nums[i-1]

            right = sum(nums) - (nums[i] + left)

            if left == right:
                return i

        return -1