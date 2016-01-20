#! bin/python

def count(ar):
	global l
	for i in xrange(100):
		l.append(ar.count(i))

m = int(raw_input())

ar = map(int,raw_input().split())

l=[]

count(ar)

result = []

for i in xrange(100):
	for j in range(l[i]):
		result.append(i)

for i in result:
	print i,
print