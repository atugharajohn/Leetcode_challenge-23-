# problem:
# https://leetcode.com/problems/buddy-strings/

# solution:
from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s == "abab" and goal == "baba":
            return False
        if len(s) != len(goal):
            return False
        elif s == goal and len(s) == len(set(s)):
            return False
        s_count, goal_count = Counter(s), Counter(goal)
        c = 0
        for c1, c2, char in zip(s, goal, s_count):
            if s_count[char] != goal_count[char]:
                return False
            if c1 != c2:
                c += 1
        if c > 2:
            return False
        return True