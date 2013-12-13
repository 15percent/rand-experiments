import sys, random
from graph import bar_graph
from random import choice

def rand_func_1():
	rand_list = [random.random() for x in range(0, 1000)]
	update_list = [int(x/0.05) for x in rand_list]
	
	count_list = [update_list.count(x) for x in range(0, 20)]
	bar_graph(count_list)

def rand_func_2():
	rand_list = [(random.random() + random.random()/2) for x in range(0, 1000)]
	update_list = [int(x/0.05) for x in rand_list]
	
	count_list = [update_list.count(x) for x in range(0, 20)]
	
	bar_graph(count_list)

def rand_func_3():
	rand_list = [random.random()*random.random() for x in range(0, 1000)]
	update_list = [int(x/0.05) for x in rand_list]
	
	count_list = [update_list.count(x) for x in range(0, 20)]
	
	bar_graph(count_list)

def rand_func_4():
	sign = [-1, 1]
	update_list = []
	for i in range(0, 10000):
		rand_list = [choice(sign) for x in range(0, 100)]
		update_list.append(sum(rand_list))

	count_list = [update_list.count(x) for x in range(-5, 6)]
	bar_graph(count_list)

def rand_func_5():
	coin = [-1, 1]
	update_list = []
	for i in range(0, 1000):
		rand_list = [choice(coin) for x in range(0, 30)]
		update_list.append(rand_list.count(1))

	count_list = [update_list.count(x) for x in range(0, 30)]
	bar_graph(count_list)

def rand_func_6(prob):
	update_list = []
	count_list = []
	for i in range(0, 1000):
		if random.random() <= prob:
			update_list.append(1)
		else:
			update_list.append(0)
	count = 0
	for i in update_list:
		if i==0:
			count = count+1
		else:
			count_list.append(count)
			count = 0
	bar_graph(count_list)

