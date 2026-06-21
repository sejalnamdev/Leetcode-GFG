class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low,high = 0,0
        f = {}
        res = float('-inf')

        for high in range(len(s)):
            f[s[high]] = f.get(s[high], 0) + 1

            length = high - low + 1
            max_count = max(f.values())
            diff = length - max_count

            while diff > k:
                f[s[low]] -= 1
                if f[s[low]] == 0:
                    del(f[s[low]])
                low += 1
                length = high - low + 1
                max_count = max(f.values())
                diff = length - max_count
            
            length = high - low + 1
            res = max(res, length)

        return res

