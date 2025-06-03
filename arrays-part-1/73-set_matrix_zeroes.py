from typing import List


class Solution1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.markRow(matrix, i)
                    self.markColumn(matrix, j)

        self.markZero(matrix)

    def markRow(self, matrix: List[List[int]], row: int):
        for j in range(len(matrix[0])):
            if matrix[row][j] != 0:
                matrix[row][j] = -1

    def markColumn(self, matrix: List[List[int]], column: int):
        for i in range(len(matrix)):
            if matrix[i][column] != 0:
                matrix[i][column] = -1

    def markZero(self, matrix: List[List[int]]):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0


class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col_markers = [1] * len(matrix[0])
        row_markers = [1] * len(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    col_markers[j] = 0
                    row_markers[i] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (row_markers[i] == 0) or (col_markers[j] == 0):
                    matrix[i][j] = 0


class Solution3:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(len(matrix[0])))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(len(matrix)))
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if (matrix[0][j] == 0) or (matrix[i][0] == 0):
                    matrix[i][j] = 0

        if first_row_has_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0


if __name__ == "__main__":
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

    Solution3().setZeroes(matrix1)
    print(matrix1)

    Solution3().setZeroes(matrix2)
    print(matrix2)
