class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        element = prices[0]
        max_dif = 0

        for i in range(1, len(prices)):

            if prices[i] < element:
                element = prices[i]

            dif = prices[i] - element

            if dif > max_dif:
                max_dif = dif

        return max_dif