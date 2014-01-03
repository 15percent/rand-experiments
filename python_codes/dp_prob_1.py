#Given 'score' for 'N' students, Give a list of 'k' students whose sum is 'S'.

import sys

score = [4, 1, 6, 2, 7, 8, 12, 3, 11, 15, 5, 13, 10, 16, 15]
N = len(score)
S = 15
k = 4

def calc(k, S, start):
	hashfunc = {x:S-x for x in score}
	if k==1 and hashfunc.has_key(S):
		print S,
		return 1
	elif k==1:
		return 0
	for i in range(start, len(score)):
		if score[i] < S:
			temp = calc(k-1, S-score[i], i+1)
			if temp==1:
				print score[i],
				return 1
	return 0




sorted(score)
temp = calc(k, S, 0)

if temp==0: print 'No such set'
