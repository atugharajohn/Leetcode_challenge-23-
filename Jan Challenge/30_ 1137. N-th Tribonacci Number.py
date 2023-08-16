# problem:
# https://leetcode.com/problems/n-th-tribonacci-number/

# solution:
class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0  # Initialize the first term of the sequence
        b = 1  # Initialize the second term of the sequence
        c = 1  # Initialize the third term of the sequence
        if n == 0:
            return 0  # If n is 0, return the first term
        if n == 1 or n == 2:
            return 1  # If n is 1 or 2, return the second or third term respectively
        for i in range(3, n+1):  # Start the loop from the third term
            d = a + b + c  # Calculate the next term in the sequence
            a = b  # Update the value of a
            b = c  # Update the value of b
            c = d  # Update the value of c
        return d  # Return the nth term