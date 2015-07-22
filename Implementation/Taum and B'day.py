T = int(raw_input())

for _ in xrange(T):
	B,W = (int(i) for i in raw_input().split())

	X,Y,Z = (int(i) for i in raw_input().split())

	if abs(X-Y)>Z:
		if X>Y:
			print Y*(B+W)+B*Z
		if Y>X:
			print X*(B+W)+W*Z
	else:
		print B*X+W*Y