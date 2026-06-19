class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        max_diff = float('inf')
        resultSum = 0

        for i in range(len(nums)-2):

            left = i+1
            right = len(nums)-1

            while left<right :

                sum = nums[i] + nums[right] + nums[left]
                diff = abs(target - sum)

                if diff < max_diff :
                    max_diff = diff
                    resultSum = sum

                if sum == target :
                    return sum

                if sum < target :
                    left += 1
                
                else :
                    right -= 1

        return resultSum
            