#!/bin/python
def quicksort(ar):
	l,r=[],[]
	p = ar[0]
	for i in range(1,len(ar)):
		if ar[i]<p:
			l.append(ar[i])
		elif ar[i]>p:
			r.append(ar[i])
	if len(l)> 1:
		l=quicksort(l)
	if len(r)> 1:
		r=quicksort(r)
	l.append(p)
	for i in l+r:
		print i,
	print
	return l+r


m = input()
ar = [int(i) for i in raw_input().strip().split()]

quicksort(ar)

#! /bin/python

def fmt(ar):
	for x in ar:
		print x,
	print

def partition(ar):
	if len(ar) < 2:
		return ar
	p = ar[0]
	smaller = [x for x in ar[1:] if x < p]
	bigger  = [x for x in ar[1:] if x > p]
	return (smaller,p,bigger)

def quickSort(ar):
	if len(ar) < 2:
		return ar
	(smaller,p,bigger)=partition(ar)
	res = quickSort(smaller)+[p]+quickSort(bigger)
	fmt(res)
	return res

m = input()
ar = [int(i) for i in raw_input().strip.split()]
quickSort(ar)