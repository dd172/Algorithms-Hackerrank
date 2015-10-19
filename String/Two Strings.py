def solution(s1,s2):
	s10 = set(s1)
	s20 = set(s2)
	result = 'NO'
	for element in s10:
		if element in s20:
			result = 'YES'
			break
	return result

if __name__ == '__main__':
	T = int(raw_input())
	for _ in range(T):
		s1 = raw_input()
		s2 = raw_input()
		print solution(s1,s2)