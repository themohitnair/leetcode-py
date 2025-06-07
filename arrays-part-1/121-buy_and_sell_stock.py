from typing import List

# AID: NeetCode for Two Pointer Solution and TuF for Dynamic Programming


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_prof = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_prof = max(max_prof, profit)
            else:
                left = right
            right += 1

        return max_prof


if __name__ == "__main__":
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [7, 6, 4, 3, 1]

    print(Solution().maxProfit(prices1))
    print(Solution().maxProfit(prices2))
