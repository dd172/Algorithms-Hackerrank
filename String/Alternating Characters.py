T=int(raw_input())

for _ in xrange(T):
	arr=raw_input()
	l=len(arr)
	count=0

	for i in xrange(l-1):

		if arr[i]==arr[i+1]:
			count+=1

	print count