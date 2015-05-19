#!/bin/python
def insertionSort(ar):  
	V=ar[-1]
	l=len(ar)
	for x in xrange(1,l):
		if ar[l-x-1]>V:
			ar[l-x]=ar[l-x-1]
			for i in ar:
				print i,
			print
		elif ar[l-x-1]==V:
			ar[l-x]=V
			for i in ar:
				print i,
			print
			break
		else:
			ar[l-x]=V
			for i in ar:
				print i,
			print
			break

		
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
