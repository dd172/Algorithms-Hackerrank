#! bin/python
#in-place quicksort //いわゆるスワープ
#divide and conquer
#O(logn)

def partition(ar,lo,hi):
	p = hi
	pivot = ar[hi]
	index = lo
	for i in xrange(lo,hi):
		if ar[i] < pivot:
			ar[i],ar[index] = ar[index],ar[i]
			index += 1
	ar[index],ar[hi] = ar[hi],ar[index]
	return index

def quickSort(ar,lo,hi):
	if lo < hi:
		p = partition(ar,lo,hi)
		quickSort(ar,lo,p-1)
		quickSort(ar,p,hi)

m = input()
ar = map(int,raw_input().strip().split())

quickSort(ar,0,m-1)

# this swap below do not need creat a new temp variant

def swap(a[i],a[j]):
	if i != j:
		a[i] += a[j]
		a[j] = a[i] - a[j]
		a[i] = a[i] - a[j]
