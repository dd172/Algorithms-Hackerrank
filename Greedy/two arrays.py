#! bin/python

def solution(A,B,N,K):
	A.sort()
	B.sort(reverse=True)
	flag = 0
	for i in xrange(N):
		if A[i]+B[i] < K:
			flag = 1
			break
	if flag:
		return 'NO'
	else:
		return 'YES'

T = int(raw_input())
for _ in xrange(T):
	(N,K) = map(int,raw_input().split())

	A = map(int,raw_input().split())
	B = map(int,raw_input().split())
	print solution(A,B,N,K)