from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        eles = []
        for row in grid:
            eles.append(row)

        eles.sort()
        to = eles[len(eles) // 2]
        tot_diff = 0

        for ele in eles:
            if ele % x != 0:
                return -1
            else:
                tot_diff = abs(ele - to)

        return tot_diff / x
