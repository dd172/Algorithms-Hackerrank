#!/bin/python
def insertionSort(ar,x):  
	V=ar[x]
	for i in range(x+1):
		if ar[i] > V:
			temp = ar[i]
			ar[i] = ar[x]
			ar[x] = temp
	for i in ar:
		print i,
	print
m = input()
ar = [int(i) for i in raw_input().strip().split()]
l = len(ar)
for x in range(1,l):
	insertionSort(ar,x)