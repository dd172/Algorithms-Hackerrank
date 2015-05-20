#!/bin/python
def insertionSort(ar):  
	V=ar[-1]
	l=len(ar)
	flag=1
	for x in xrange(l):
		if x==l-1:
			ar[l-x-1]=V
		else:
			if ar[l-x-2]>V:
				ar[l-x-1]=ar[l-x-2]	
			elif ar[l-x-2]==V:
				flag=0
			else:
				ar[l-x-1]=V
				flag=0
		for i in ar:
			print i,
		print
		if not flag:
			break
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
