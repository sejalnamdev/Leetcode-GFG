class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxending = nums[0]
        minending = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):

            v1 = maxending * nums[i]
            v2 = minending * nums[i]
            v3 = nums[i]

            maxending = max(v1, max(v2,v3))
            minending = min(v1, min(v2,v3))
            res  = max(res, max(maxending,minending))

        return res