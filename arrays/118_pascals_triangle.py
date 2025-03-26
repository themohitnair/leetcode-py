from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(0, numRows - 1):
            prev_row = [0] + triangle[i] + [0]
            row = []
            for i in range(len(prev_row) - 1):
                row.append(prev_row[i] + prev_row[i + 1])
            triangle.append(row)

        return triangle


print(Solution().generate(5))
