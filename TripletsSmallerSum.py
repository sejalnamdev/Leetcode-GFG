class Solution:
    def countTriplets(self, sum, arr):
        #code here
        arr.sort()
        ans = 0
        
        for i in range(len(arr)-2):
            left = i+1
            right = len(arr)-1
            
            while left < right :
                actualsum = arr[i]+arr[left]+arr[right]
               
                
                if actualsum < sum :
                    ans = ans + (right - left)
                    left += 1
                    
                else :
                    right -= 1
                    
        return ans
        