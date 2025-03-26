from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        row_dec = any(matrix[0][c] == 0 for c in range(COLS))
        col_dec = any(matrix[r][0] == 0 for r in range(ROWS))

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if not matrix[r][c]:
                    matrix[0][c], matrix[r][0] = 0, 0

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if not matrix[0][c] or not matrix[r][0]:
                    matrix[r][c] = 0

        if row_dec:
            for c in range(COLS):
                matrix[0][c] = 0

        if col_dec:
            for r in range(ROWS):
                matrix[r][0] = 0
