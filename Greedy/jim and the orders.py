#! bin/python

def solution(ar,dic):
	res = [0]*len(ar)
	sorted_ar = sorted(ar)
	for i in range(len(res)):
		res[i]=ar.index(sorted_ar[i]) + 1
		ar[ar.index(sorted_ar[i])]=0
	for i in res:
		print i,
	print


N = int(raw_input())

ar=[]
dic=[]
res=[]
for i in xrange(N):
	(t,d) = map(int,raw_input().split())
	dic.append(t)
	ar.append(t+d)

solution(ar,dic)
