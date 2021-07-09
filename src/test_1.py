# What are the two primary weaknesses of a static array as a data structure?

# 1. Fixed size
# 2. O(n) insertions and deletions



# What is the time complexity of slicing an array in Python?

# Time: O(n)
# Space: O(n)



# Why are out-of-place algorithms generally considered to be safer?

# Because they avoid side-effects


# In your own words, explain why the worst-case time case of appending to dynamic array is O(n).

# Appending to a dynamic array is the worst-case time cost of O(n) is due to the fact that if our array has a 
# capacity of 10 and we append more items to it, a new static array is made with double the capacity in order to
# store all the values from the original array WITH the new values we want to be appended in. If we have an array
# with 110 values and append 1000 values to it, the new array created will be 220, and will then have another 
# created after that that is also double, 440, and so on until a large enough array is created to account for all
# the appended values. This is computationally expensive!


'''
You are given the prices of a stock, in the form of an array of integers, prices. Let's say that prices[i] is the price of the stock on the ith day (0-based index). Assuming that you are allowed to buy and sell the stock only once, your task is to find the maximum possible profit (the difference between the buy and sell prices).

Note: You can assume there are no fees associated with buying or selling the stock.

Example:


For prices = [6, 3, 1, 2, 5, 4], the output should be buyAndSellStock(prices) = 4.

It would be most profitable to buy the stock on day 2 and sell it on day 4. Thus, the maximum profit is
 prices[4] - prices[2] = 5 - 1 = 4.

For prices = [8, 5, 3, 1], the output should be buyAndSellStock(prices) = 0.

Since the value of the stock drops each day, there's no way to make a profit from selling it. Hence, the maximum 
profit is 0.

For prices = [3, 100, 1, 97], the output should be buyAndSellStock(prices) = 97.

It would be most profitable to buy the stock on day 0 and sell it on day 1. Thus, the maximum profit is 
prices[1] - prices[0] = 100 - 3 = 97.
'''


def buyAndSellStock(prices):
    maxProfit = 0
    buyPrice = 0
    sellPrice = 0
    updateBuyPrice = True
    for i in range(len(prices) - 1):
        sellPrice = prices[i + 1]
        if updateBuyPrice:
            buyPrice = prices[i]
        if sellPrice < buyPrice:
            buyPrice = sellPrice
        else:
            currentProfit = sellPrice - buyPrice
            if currentProfit > maxProfit:
                maxProfit = currentProfit
                updateBuyPrice = False
    return maxProfit


print(buyAndSellStock([6, 3, 1, 2, 5, 4]))
print(buyAndSellStock([3, 100, 1, 97]))
