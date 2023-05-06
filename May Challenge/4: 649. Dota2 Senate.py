# problem:
# https://leetcode.com/problems/dota2-senate/

# solution:
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque(i for i, c in enumerate(senate) if c == 'R')
        dire = deque(i for i, c in enumerate(senate) if c == 'D')

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()

        return 'Radiant' if radiant else 'Dire'