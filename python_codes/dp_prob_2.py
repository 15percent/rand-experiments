# One more DP question. You are Captain Hindsight, you go tell stock market traders how much money they could have made at maximum after looking at a time series of stock prices. The problem is: Given a list of prices as seen each day, find the buying and selling days which give the highest profit. (buying has to happen before selling)

# Suppose input is [9, 6, 7, 8, 13, 5]
# answer is day buy on day 2 sell on day 5

import sys

#a = [9, 6, 7, 8, 13, 5]
#a = [3, 7, 12, 4, 5, 15, 1, 6, 9, 11, 4]
a = [5, 4, 3, 2, 4]
min_index = 0
max_profit = a[0] - a[min_index]

for i in range(0, len(a)):
	if a[i] < a[min_index]: min_index = i
	if (a[i] - a[min_index]) > max_profit:
		max_profit = (a[i] - a[min_index])
		buy = min_index
		sell = i

print 'Buy on day',buy+1,'Sell on day',sell+1
