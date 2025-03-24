class Solution(
    object
):  # four steps: find number before decreasing spell, find rightmost number that is greater than that number, swap those two, and reverse the section of the list after the first number
    def nextPermutation(self, nums):
        END = len(nums) - 1

        ind1, ind2 = -1, -1
        for i in range(END - 1, -1, -1):
            if nums[i] < nums[i + 1]:
                ind1 = i
                break

        if ind1 == -1:
            nums.reverse()
        else:
            for i in range(END, ind1, -1):
                if nums[i] > nums[ind1]:
                    ind2 = i
                    break

            nums[ind1], nums[ind2] = nums[ind2], nums[ind1]

            nums[ind1 + 1 :] = nums[ind1 + 1 :][::-1]
