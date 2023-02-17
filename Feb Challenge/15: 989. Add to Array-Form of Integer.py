# problem:
# https://leetcode.com/problems/add-to-array-form-of-integer/

# solution:
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return list(map(int,str( int(''.join(map(str,num)))+k )))