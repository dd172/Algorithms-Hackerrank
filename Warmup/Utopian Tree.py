#!/usr/bin/env python
#Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def solution(N):
		h=1
		for x in range(1,N+1):
			if x&1:
				h*=2
			else:
				h+=1
		return h
        
if __name__ == '__main__':
	T=int(sys.stdin.readline())
	for _ in range(T):
		N=int(sys.stdin.readline())
		print solution(N)