from typing import List


# AID: Kadane's Algorithm
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)

        return max_sum


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum


if __name__ == "__main__":
    print(Solution2().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
