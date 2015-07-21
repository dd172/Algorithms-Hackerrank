# Enter your code here. Read input from STDIN. Print output to STDOUT

def solution(A):
	print len(A)
	for i in range(len(A)):
		A[i]=A[i]-min(A)
	print "删除0元素前"
	print A
	for _ in A:
		if _==0:
			A.remove(_)
	print "删除0元素后"
	print A
	if(len(A)):
		solution(A)

if __name__ == '__main__':
	N=raw_input()
	A=map(int,raw_input().split())
	solution(A)