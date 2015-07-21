# Enter your code here. Read input from STDIN. Print output to STDOUT

def solution(n,a,b):
	res=[]
	for i in range(n):
		number=(n-i-1)*a+i*b
		res.append(number)
	res=list(set(res))
	res.sort()
	for i in res:
		print i,
	print


if __name__ == '__main__':
	T=int(raw_input())
	for _ in xrange(T):
		n=int(raw_input())
		a=int(raw_input())
		b=int(raw_input())
		solution(n,a,b)
