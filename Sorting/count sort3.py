#! bin/python

def count(ar):
	global l
	for i in xrange(100):
		l.append(ar.count(i))

m = int(raw_input())
ar1,ar2,ass_ar,l= [],[],[],[]

for _ in xrange(m):
	left,right = raw_input().split()
	ar1.append(int(left))
	ar2.append(right)


count(ar1)


for i in range(len(l)):
	if i:
		l[i]=l[i-1]+l[i]

for i in l:
	print i,
print