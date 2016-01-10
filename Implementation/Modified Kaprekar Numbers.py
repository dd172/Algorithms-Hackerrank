P=int(raw_input())
Q=int(raw_input())
k=P
count = 0
while k<=Q:
	kx2=k*k
	kx2s = str(kx2)
	if len(kx2s)%2:
		m=(len(kx2s)+1)/2-1
	else:
		m=len(kx2s)/2

	l = kx2s[0:m]
	r = kx2s[m:]
	#print l,r
	r = int(r)
	if not len(l): 
		l=0
	elif not int(l):
		continue
	else:
		l=int(l)
	if k == l+r:
		print k,
		count += 1	
	k += 1
if not count:
	print 'INVALID RANGE'
