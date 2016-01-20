#! bin/python

def count(ar):
	global l
	for i in xrange(100):
		l.append(ar.count(i))

m = int(raw_input())

ar = map(int,raw_input().split())

l=[]

count(ar)

for i in l:
	print i,
print