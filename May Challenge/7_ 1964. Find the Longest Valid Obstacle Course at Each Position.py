# problem:
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

# solution:
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        dp = [1] * n
        stack = [obstacles[0]]
        for i in range(1, n):
            if obstacles[i] >= stack[-1]:
                dp[i] = len(stack) + 1
                stack.append(obstacles[i])
            else:
                idx = bisect.bisect_right(stack, obstacles[i])
                dp[i] = idx + 1
                stack[idx] = obstacles[i]
        return dp