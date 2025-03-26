from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        eles = []
        for row in grid:
            eles += row

        if len(eles) == 1:
            return 0

        eles.sort()
        to = eles[len(eles) // 2]
        tot_diff = 0

        for ele in eles:
            tot_diff += abs(ele - to)
            if tot_diff % x != 0:
                return -1

        return tot_diff // x
