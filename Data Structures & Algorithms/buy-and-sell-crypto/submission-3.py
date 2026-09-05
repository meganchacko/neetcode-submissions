class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # what i need to do : dynamic sliding window
        # starts at first, assigns it buy and the next is sell
        # if negative profit, immediately shift both +1
        # else, move sell to the next day 
        buy = 0 
        sell = 1 
        max_profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                curr_profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, curr_profit)
            else:
                buy = sell         
            sell+=1

        return max_profit

