# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 리트코드 121. Best Time to Buy and Sell Stock
# 최고 이익 낼 수 있는 매수 매도 타이밍 구하기

from typing import List
import sys

test_case = [7, 1, 5, 3, 6, 4]


def buy_sell_stock_my(nums: List[int]) -> int:
    min_price = nums[0]
    max_gap = 0

    for price in nums:
        if price <= min_price:
            min_price = price
        else:
            if price - min_price > max_gap:
                max_gap = price - min_price

    return max_gap


def buy_sell_stock_sol2(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    # 최소값, 최대수익 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


print(buy_sell_stock_my(test_case))
print(buy_sell_stock_sol2(test_case))
