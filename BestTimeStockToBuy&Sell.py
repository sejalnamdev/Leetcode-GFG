class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for i in range(len(prices)):
            maxProfit = max( prices[i]-minPrice , maxProfit )
            minPrice = min(prices[i] , minPrice )

        return maxProfit
        return minPrice