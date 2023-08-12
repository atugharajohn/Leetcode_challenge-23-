# problem:
# https://leetcode.com/problems/asteroid-collision/

# solution:
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]: 
        stack = []
        for a in asteroids:
            #collision will happen only when top is going right and a is going left
            while stack and stack[-1] > 0 and a < 0:
                diff = stack[-1] + a
                if diff < 0: #top of stack is smaller 
                    stack.pop()
                elif diff > 0: #top of stack is larger
                    a = 0
                else: #same magnitude
                    a = 0
                    stack.pop()
            if a: #if stack becomes empty or top and a have same direction
                stack.append(a)
        return stack
        