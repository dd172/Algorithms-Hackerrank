def solution(s):
	s0 = set(s)
	odd = 0
	for element in s0:
		if s.count(element)%2:
			odd += 1

	if len(s)%2:
		if odd > 1:
			return 'NO'
		else:
			return 'YES'
	else:
		if odd:
			return 'NO'
		else:
			return 'YES'


if __name__ == '__main__':
	s = raw_input()
	print solution(s)

