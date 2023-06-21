# problem:
# https://leetcode.com/problems/make-array-strictly-increasing/

# solution:
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        @cache
        def dfs(i, x):
            if i == len(arr1): return 0
            j = bisect_left(arr2, x+1)
            return min(
                dfs(i+1, arr2[j]) + 1 if j < len(arr2) else 2001,
                dfs(i+1, arr1[i]) if arr1[i] > x else 2001
            )

        res = dfs(0, -1)
        if res != 2001: return res
        return -1