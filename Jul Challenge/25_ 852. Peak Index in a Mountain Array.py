# problem:
# https://leetcode.com/problems/peak-index-in-a-mountain-array/

# solution:
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        while low <= high:
            i = low + (high - low) // 2
            if arr[i - 1] < arr[i] < arr[i + 1]:
                low = i
            if arr[i - 1] > arr[i] > arr[i + 1]:
                high = i
            if arr[i - 1] < arr[i] > arr[i + 1]:
                return i