n=int(raw_input())
x=[]
res=[]
for i in xrange(n):
	x.append(raw_input())
res.append(x[0])
for i in xrange(1,n-1):
	res.append(x[i][0])
	for j in xrange(1,n-1):
		mid=x[i][j]
		top=x[i-1][j]
		bottom=x[i+1][j]
		right=x[i][j+1]
		left=x[i][j-1]
		if mid > top and mid > bottom and mid > right and mid > left:
			res[i] += 'X'
		else:
			res[i] += x[i][j]
	res[i] += x[i][-1]
res.append(x[-1])
for i in xrange(n):
	print res[i]