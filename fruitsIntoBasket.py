class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        f = {}
        res = 0

        for right in range(len(fruits)):

            f[fruits[right]] = f.get(fruits[right], 0) + 1

            while len(f) > 2:
                f[fruits[left]] -= 1

                if f[fruits[left]] == 0:
                    del f[fruits[left]]

                left += 1

            length = right - left + 1
            res = max(res, length)

        return res