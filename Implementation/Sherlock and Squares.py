# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def solution(A,B):
	A=float(A)
	B=float(B)
	sra=math.sqrt(A)
	srb=math.sqrt(B)
	A_=int(math.ceil(sra))
	B_=int(math.floor(srb))
	return B_-A_+1
if __name__ == '__main__':
	T=int(raw_input())

	for _ in xrange(T):
		A,B=raw_input().split()
		print solution(A,B)

