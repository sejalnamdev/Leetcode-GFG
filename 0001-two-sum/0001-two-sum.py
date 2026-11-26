class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mp = {}
        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in mp :
                return mp[compliment],i

            mp[nums[i]] = i