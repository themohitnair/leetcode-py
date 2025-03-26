from typing import List


class Solution:  # O(n), O(1)
    def sortColors(self, nums: List[int]) -> None:
        l, m, r = 0, 0, len(nums) - 1

        while m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[r], nums[m] = nums[m], nums[r]
                r -= 1


class AnotherSolution:
    def sortColors(self, nums: List[int]) -> None:
        size = 3
        count = [0] * size

        for i in nums:
            count[i] += 1

        index = 0
        for i in range(len(count)):
            while count[i] > 0:
                nums[index] = i
                index += 1
                count[i] -= 1


nums = [2, 0, 2, 1, 1, 0]
AnotherSolution().sortColors(nums)
print(nums)
