from typing import List


class Solution:  # Kadane algorithm O(n), O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        maxSum = -100000
        for num in nums:
            s += num
            maxSum = max(maxSum, s)
            if s < 0:
                s = 0
        return maxSum
