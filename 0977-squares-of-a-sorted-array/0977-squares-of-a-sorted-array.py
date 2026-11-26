class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        pos = []
        neg = []

        for i in range(len(nums)):
            if nums[i] >= 0:
                pos.append(nums[i]*nums[i])

            else:
                neg.append(nums[i]*nums[i])

        if neg:
            neg.reverse()   

        i = 0
        j = 0
        idx = 0
        n = len(pos)
        m = len(neg)

        while i < len(pos) and j < len(neg):

            if pos[i] < neg[j] :
                nums[idx] = pos[i]
                i += 1
                idx += 1

            else:
                nums[idx] = neg[j]
                j += 1
                idx += 1

        while i < n:
            nums[idx] = pos[i]
            idx += 1
            i += 1

        while j < m:
            nums[idx] = neg[j]
            idx += 1
            j += 1



        return nums
             
