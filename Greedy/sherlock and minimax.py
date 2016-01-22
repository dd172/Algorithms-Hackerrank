#! bin/python

def solution(A,P,Q):

	l1 = []
	l2 = []
	l3 = []
	for i in xrange(len(A)-1):
		l1.append((A[i+1]+A[i])/2)
		l2.append((A[i+1]-A[i])/2)
	l1.append(P)
	l1.append(Q)
	p = min([abs(P-A[v]) for v in range(len(A))])
	q = min([abs(Q-A[v]) for v in range(len(A))])
	l2.append(p)
	l2.append(q)
	for i in l1:
		if i < P:
			l2[l1.index(i)] = 0
		if i > Q:
			l2[l1.index(i)] = 0


	#rint l1
	#rint l2
	MAX = max(l2)

	for i in range(len(l2)):
		if l2[i] == MAX:
			l3.append(l1[i])
	#rint l3
	print min(l3)



	

N = int(raw_input())

A = map(int,raw_input().split())

(P,Q) = map(int,raw_input().split())

A.sort()
#print A
solution(A,P,Q)