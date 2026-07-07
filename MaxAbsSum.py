class Solution:
    def maxsumsubarray(self, nums: List[int]) -> int:
        bestending = nums[0]
        ans1 = nums[0]

        for i in range(1, len(nums)):
            v1 = nums[i]
            v2 = bestending + nums[i]

            bestending = max(v1, v2)
            ans1 = max(ans1, bestending)

        return ans1

    def minsumsubarray(self, nums: List[int]) -> int:
        bestending = nums[0]
        ans2 = nums[0]

        for i in range(1, len(nums)):
            v1 = nums[i]
            v2 = bestending + nums[i]

            bestending = min(v1, v2)
            ans2 = min(ans2, bestending)

        return ans2


    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = abs(self.maxsumsubarray(nums))
        min_sum = abs(self.minsumsubarray(nums))

        res = max(max_sum, min_sum)

        return res