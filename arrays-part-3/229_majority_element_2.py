from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2, count1, count2 = None, None, 0, 0

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        threshold = len(nums) // 3
        majs = []
        if nums.count(candidate1) > threshold:
            majs.append(candidate1)
        if nums.count(candidate2) > threshold:
            majs.append(candidate2)

        return majs
