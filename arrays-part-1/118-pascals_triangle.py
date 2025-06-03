from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        seed = [[1]]
        if numRows == 1:
            return seed

        else:
            row = 1
            while row < numRows:
                buff = [0] + seed[row - 1] + [0]
                next_row = []
                for i in range(len(buff) - 1):
                    next_row.append(buff[i] + buff[i + 1])
                seed.append(next_row)
                row += 1

        return seed


if __name__ == "__main__":
    print(Solution().generate(5))
    print(Solution().generate(1))
