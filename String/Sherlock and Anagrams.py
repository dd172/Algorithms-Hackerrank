def solution(s):
	count = 0
	lng = len(s)
	r1,r2 = 1,2
	for range in xrange(1,lng):
		for i in xrange(lng-range):
			for j in xrange(i+1,lng +1 - range):
				if sorted(s[i:i+range]) == sorted(s[j:j+range]):
					count +=1
	return count

if __name__ == '__main__':
	T = int(raw_input())
	for _ in range(T):
		s = raw_input()
		print solution(s)