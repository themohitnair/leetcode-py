class Solution1(
    object
):  # DIY, good solution, but doesn't beat most solutions, and is two-pass
    def sortColors(self, nums):
        size = 3
        count = [0] * size

        for i in nums:
            count[i] += 1

        index = 0
        for i in range(size):
            while count[i] > 0:
                nums[index] = i
                count[i] -= 1
                index += 1


class Solution2(object):  # Dutch National Flag Algorithm, one-pass
    def sortColors(self, nums):
        left, mid, right = 0, 0, len(nums) - 1
        while mid <= right:
            if nums[mid] == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
