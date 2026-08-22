class Solution:
    def checkDivisibility(self, n: int) -> bool:

        original = n
        digitsum = 0
        productsum = 1

        while n:
            digit = n % 10
            n = n // 10

            digitsum += digit
            productsum *= digit

        if original % (digitsum + productsum) == 0:
            return True

        return False

        