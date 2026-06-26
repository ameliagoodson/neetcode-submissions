class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        left = 0
        right = 1
        profit = 0

        while right < len(prices):
            #is it profitable
            if prices[left] < prices[right]:
                profit = max(profit, prices[right] - prices[left])
            # if we found a new low price, shift left to right pointer
            else:
                left = right
            right += 1
        return profit


