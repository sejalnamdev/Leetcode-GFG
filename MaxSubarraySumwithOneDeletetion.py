class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_delete = arr[0]
        one_delete = float('-inf')
        res = arr[0]

        for i in range(1, len(arr)):

            Prev_no_delete = no_delete
            Prev_one_delete = one_delete

            no_delete = max(arr[i], no_delete + arr[i])

            if Prev_one_delete == float('-inf'):
                v1 = arr[i]
            else:
                v1 = arr[i] + Prev_one_delete

            one_delete = max(v1, Prev_no_delete)

            res = max(res, max(no_delete, one_delete))

        return res