class Solution:

    def fun(self, n:int) -> int:
        sum = 0
        while n>0:
            d=n%10
            n=n//10
            sum = sum + d*d
        return sum

    def isHappy(self, n: int) -> bool:
        slow, fast = n,n
        while fast != 1:
            slow = self.fun(slow)
            fast = self.fun(fast)
            fast = self.fun(fast)

            if slow == fast and slow != 1:
                return False
        
        return True

        