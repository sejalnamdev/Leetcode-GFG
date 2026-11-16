class Solution:
    def digitSum(self, s: str, k: int) -> str:
       
        
        while len(s) > k:
            c = ""
            for i in range(0,len(s),k):
                c += str(sum(int(p) for p in s[i:i+k]))
            s = c

        return s
