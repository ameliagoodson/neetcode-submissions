class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force - nested loop
        # max profit variable
        # first price. iterate and keep variable of highest price to compare to
        # each iteration has to start from the ith index not the start
        profit = 0

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i] < prices[j]:
                    prelimprofit = prices[j] - prices[i]
                    if prelimprofit > profit:
                        profit = prelimprofit
                    
        return profit

