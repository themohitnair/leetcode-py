from typing import List

# Dutch National Flag Algorithm or Reconstruction


class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0] * 3
        for i in nums:
            counts[i] += 1

        start = 0
        for i in range(len(counts)):
            while counts[i] > 0 and start < len(nums):
                nums[start] = i
                start += 1
                counts[i] -= 1


class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1


if __name__ == "__main__":
    nums1 = [2, 0, 2, 1, 1, 0]
    nums2 = [2, 0, 1]

    Solution2().sortColors(nums1)
    Solution2().sortColors(nums2)

    print(nums1)
    print(nums2)
