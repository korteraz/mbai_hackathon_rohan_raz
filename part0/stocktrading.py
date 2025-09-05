#Raz Kurteran and Rohan Kumar
def maxProfit(prices):
    if len(prices) == 0:
        return 0
    buy_price = prices[0]
    max_profit = 0
    for price in prices:
        buy_price = min(price, buy_price)
        max_profit = max(max_profit, price - buy_price)
    return max_profit

if __name__ == '__main__':
    print(maxProfit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(maxProfit([3,2,1]))
    print(maxProfit([0,0,0]))
    print(maxProfit([3,1,3]))
    print(maxProfit([]))