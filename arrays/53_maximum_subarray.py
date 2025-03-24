class Solution(object):  # Kadane algo linear. others lead to TLE (cubic and quadratic)
    def maxSubArray(self, nums):
        m = -100000
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            m = max(s, m)
            if s < 0:
                s = 0

        return m
