def solution(s):
	s0 = list(s)
	lng = len(s)

	for i in range(lng):
		if s0[lng - 2 - i] < s0[lng - 1 - i]:
			s1=list(s0[0:lng - i - 1])
			s2=list(s0[lng - i - 1:lng])
			if not s1:
				continue
			s2.sort()
			for i in range(len(s2)):
				if s2[i] > s1[-1]:
					temp = s1[-1]
					s1[-1]=s2[i]
					s2[i]=temp
					s2.sort()

					break
			s10=''.join(s1)
			s20=''.join(s2)
			return s10+s20
			break
	else:
		return 'no answer'


if __name__ == '__main__':
	T = int(raw_input())
	for _ in range(T):
		s = raw_input()
		print solution(s)