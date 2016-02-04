#!/bin/python
import math

def solution(K,C):
	C.sort(reverse=True)
	print C
	print C[20]
	k = 0
	x = 0
	for i in xrange(len(C))
:		if k < K: 
			k += 1
		elif k == K:
			k = 0
			x += 1
		C[i] = (x + 1)*C[i]

	print C
	return sum(C)




# code snippet illustrating input/output methods 
N, K = raw_input().split()
N = int(N)
K = int(K)
C = []

numbers = raw_input()

i = 0
for number in numbers.split():
   C.append( int(number) )
   i = i+1

result = solution(K,C)
print result
