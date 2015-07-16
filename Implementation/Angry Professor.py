T=int(raw_input())

for _ in xrange(T):
	N,K=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	
	count = 0

	for time in arr:
		if time <= 0:
			count+=1

	if count >= K:
		print 'NO'
	else:
		print 'YES'