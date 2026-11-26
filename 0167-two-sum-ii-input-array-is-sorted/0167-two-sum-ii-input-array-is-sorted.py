class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        arr = []

        mp = {}

        for i in range(len(numbers)):
            compliment = target - numbers[i]

            if compliment in mp:
                return mp[compliment]+1, i+1

            mp[numbers[i]] = i