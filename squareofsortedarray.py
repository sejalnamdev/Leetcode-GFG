class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos =[]

        neg = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                pos.append(nums[i])
            else :
                neg.append(nums[i])
            
            #poora negative
        if len(pos) == 0 :
            for i in range(len(neg)):
                neg[i] = neg[i]*neg[i]
                    
            neg.reverse()
            return neg
            
            #poora positive
        if len(neg) == 0 :
            for i in range(len(pos)):
                pos[i] = pos[i]*pos[i]
            return pos

        
        idx = 0
        n = len(neg)
        m = len(pos)
        res = []
        

        for i in range(len(neg)) :
            neg[i] = neg[i]*neg[i]
        neg.reverse()

        for i in range(len(pos)) :
            pos[i] = pos[i]*pos[i]

        i = 0
        j = 0

        while i<n and j<m :
            if neg[i] <= pos[j] :
                res.append(neg[i])
                idx += 1
                i += 1
            else : 
                res.append(pos[j])
                idx += 1
                j += 1

        while i < n :
            res.append(neg[i])
            idx += 1
            i += 1
        while j < m :
            res.append(pos[j])
            idx += 1
            j += 1
        return res




         