class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = prices[0]   # sabse sasta buying price
        max_profit = 0

        for price in prices:

            # agar aur sasta mila to buy update
            if price < min_price:
                min_price = price

            # current profit calculate
            profit = price - min_price

            # maximum profit update
            max_profit = max(max_profit, profit)

        return max_profit