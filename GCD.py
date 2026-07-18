class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)

        for i in range(1,min(mini, maxi)+1):
            if mini % i == 0 and maxi % i ==0 :
                x = i                
        return x