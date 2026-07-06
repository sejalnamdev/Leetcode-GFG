class Solution:
    def smallestSumSubarray(self, A, N):
        #Your code here
        bestending = A[0]
        res = A[0]
        
        for i in range(1,len(A)):
            
            v1 = A[i]
            v2 = bestending + A[i]
            
            bestending = min(v1, v2)
            res = min(res, bestending)
            
        return res
        