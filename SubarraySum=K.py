class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        f = {}
        f[0] = 1
        res = 0

        for i in range(len(nums)):
            sum += nums[i]
            ques = sum - k

            freq = f.get(ques, 0)

            res += freq

            f[sum] = f.get(sum, 0) + 1

        return res