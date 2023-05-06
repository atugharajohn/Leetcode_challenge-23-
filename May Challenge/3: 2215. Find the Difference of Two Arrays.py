# problem:
# https://leetcode.com/problems/find-the-difference-of-two-arrays/

# solution:
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1).difference(set(nums2))),list(set(nums2).difference(set(nums1)))]