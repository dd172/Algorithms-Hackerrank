def solution(N):
	count=0
	n=int(N)
	for I in N:
		i=int(I)
		if i!=0:
			if n%i == 0:
				count+=1
	return count

if __name__ == '__main__':
	T = int(raw_input())
	for _ in xrange(T):
		N=raw_input()
		print solution(N)