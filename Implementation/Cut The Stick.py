def solution(L):
	L.sort(reverse=True)
	while len(L)>0:
		print len(L)
		block_cut=L.pop()
		while len(L)>0 and L[-1]<=block_cut:
			L.pop()

if __name__ == '__main__':
	T = int(raw_input())
	for _ in xrange(T):
		L=map(int,raw_input().split())
		solution(L)
