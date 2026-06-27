class Solution:

    def fun(self, have, need):
        for i in range(256):
            if have[i]<need[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        have = [0]*256
        need = [0]*256

        if n<m:
            return ""

        for i in range(m):
            need[ord(t[i])] += 1

        low = 0
        res = float('inf')
        start = -1

        for high in range(n):
            have[ord(s[high])] += 1

            while self.fun(have, need):
                length = high - low + 1

                if length < res:
                    res = length
                    start = low

                have[ord(s[low])] -= 1
                low += 1
        
        if res == float('inf'):
            return ""
        
        return s[start:start + res]


        


