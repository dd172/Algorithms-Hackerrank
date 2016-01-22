#! bin/python
def solution(grid):
	for line in grid:
		line.sort()
	flag = 0
	for line in zip(*grid):
		if list(line) != sorted(line):
			flag=1
			break
	if flag:
		print 'NO'
	else:
		print 'YES'

if __name__ == '__main__':
	T = int(raw_input())

	for _ in xrange(T):
		N = int(raw_input())
		grid=[]
		for i in xrange(N):
			grid.append(list(raw_input()))
		solution(grid)

