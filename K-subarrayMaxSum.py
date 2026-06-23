class Solution:
    def maxSubarraySum(self, arr, k):

        low = 0
        high = k
        window_sum = 0

        for i in range(k):
            window_sum += arr[i]

        res = window_sum

        while high < len(arr):
            window_sum = window_sum - arr[low] + arr[high]

            low += 1
            high += 1

            res = max(res, window_sum)

        return res