# Given an array of numbers representing the stock prices of a company in 
# chronological order, write a function that calculates the maximum profit 
# you could have made from buying and selling that stock once. Note that you
#  must buy before you can sell it.
# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
# Example of different list of stock prices and respective outputs.
# List = [75,73,60,100,120,130]
# Output = 70
# List = [10,20,23,22,17,30]
# Output = 20
# List = [1,6,19,59,30,60]
# Output = 59
def buy_and_sell(arr):
  max_profit=0
  liste =[]
  for i in range(len(arr)-1):
    for j in range(i,len(arr)):
      buy_price=arr[i]
      sell_price=arr[j]
      max_profit=max(max_profit,sell_price-buy_price)
  return max_profit
  print(max(liste))
buy_and_sell([9, 11, 8, 5, 7, 10])