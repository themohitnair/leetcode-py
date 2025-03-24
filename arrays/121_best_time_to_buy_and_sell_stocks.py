class Solution1(object):  # best solution, one-pass
    def maxProfit(self, prices):
        maxP = 0
        minP = prices[0]

        for price in prices:
            if price < minP:
                minP = price
            elif price - minP > maxP:
                maxP = price - minP

        return maxP


class Solution2(object):
    def maxProfit(self, prices):
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[r] >= prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1
        return maxP


print(Solution2().maxProfit([7, 1, 5, 3, 6, 4]))
