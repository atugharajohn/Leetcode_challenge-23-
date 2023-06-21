# problem:
# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

# solution:
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def calc_sum(cnt, end):
            if cnt == 0:
                return 0
            start = max(end - cnt, 0)
            sum1 = end * (1 + end) // 2
            sum2 = start * (1 + start) // 2
            return sum1 - sum2

        maxSum -= n
        l, r = 0, maxSum
        while l <= r:
            mid = (l + r) // 2
            left_sum = calc_sum(index + 1, mid)
            right_sum = calc_sum(n - index - 1, mid - 1)
            if left_sum + right_sum <= maxSum:
                l = mid + 1
            else:
                r = mid - 1
        return l