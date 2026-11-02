class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)

        nums.sort()

        median = nums[n // 2]
        moves = 0

        for i in range(n):
            moves += abs(nums[i] - median)

        return moves