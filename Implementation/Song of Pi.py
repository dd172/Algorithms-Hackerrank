def solution(Arr):
	Pi='31415926535897932384626433833'
	arr=Arr.split()
	flag=0
	for i in xrange(len(arr)):
		if int(Pi[i])!=len(arr[i]):
			flag=1
	if flag:
		return 'It\'s not a pi song.'
	else:
		return 'It\'s a pi song.'

if __name__ == '__main__':
	T = int(raw_input())
	for _ in xrange(T):
		Arr=raw_input()
		print solution(Arr)
