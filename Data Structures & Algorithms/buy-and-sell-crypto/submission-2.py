class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProf = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            if (prices[right] - prices[left]) > maxProf:
                maxProf = prices[right] - prices[left]
            right += 1
        
        return maxProf

