# One more DP question. You are Captain Hindsight, you go tell stock market traders how much money they could have made at maximum after looking at a time series of stock prices. The problem is: Given a list of prices as seen each day, find the buying and selling days which give the highest profit. (buying has to happen before selling)

# Suppose input is [9, 6, 7, 8, 13, 5]
# answer is day buy on day 2 sell on day 5

import sys

#a = [9, 6, 7, 8, 13, 5]
#a = [3, 7, 12, 4, 5, 15, 1, 6, 9, 11, 4]
a = [5, 4, 3, 2, 4]
hashtab = {}
min_num = a[0]
min_index = 0

for i in range(0, len(a)):
	if a[i] < min_num:
		min_num = a[i]
		min_index = i
	hashtab[(a[i], i)] = (min_num, min_index)

max_num = a[0] - hashtab[(a[0], 0)][0]
max_index = 0

for i in range(0, len(a)):
	if (a[i] - hashtab[(a[i], i)][0]) > max_num:
		max_num = (a[i] - hashtab[(a[i], i)][0])
		max_index = i

print 'Buy on day',hashtab[(a[max_index], max_index)][1]+1,'sell on day',max_index+1
