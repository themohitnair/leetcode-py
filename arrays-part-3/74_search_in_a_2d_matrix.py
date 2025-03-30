from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        low, high = 0, (r * c) - 1

        while low <= high:
            mid = (low + high) // 2
            row_mid, col_mid = mid // c, mid % c

            if matrix[row_mid][col_mid] == target:
                return True
            elif target < matrix[row_mid][col_mid]:
                high = mid - 1
            else:
                low = mid + 1

        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(Solution().searchMatrix(matrix, target))
