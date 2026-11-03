class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        maxi = max(nums)

        for i in range(n):
            ans += abs(nums[i] - maxi)

        return ans