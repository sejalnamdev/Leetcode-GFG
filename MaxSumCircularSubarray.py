class Solution:
    def minSubarraySum(self, nums: List[int]) -> int:
        bestending = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            v1 = nums[i]
            v2 = bestending + nums[i]
            bestending =min(v1,v2)
            ans = min(ans, bestending)
        return ans

    def maxSubarraySum(self, nums: List[int]) -> int:
        bestending = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            v1 = nums[i]
            v2 = bestending + nums[i]
            bestending =max(v1,v2)
            ans = max(ans, bestending)
        return ans

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        TotalSum = sum(nums)
        
        normal = self.maxSubarraySum(nums)
        if normal < 0:
            return normal

        circular = TotalSum - self.minSubarraySum(nums)

        res = max(normal, circular)

        return res
        