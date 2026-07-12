class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero = 0
        one = 0
        res = 0
        f = {}

        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                one += 1

            diff = zero - one

            if diff == 0:
                res = max(res, i+1)
            
            if diff not in f:
                f[diff] = i                     #f[diff] = f.get(diff, i)
            else:
                idx = f[diff]
                length = i - idx
                res = max(res, length)

        return res