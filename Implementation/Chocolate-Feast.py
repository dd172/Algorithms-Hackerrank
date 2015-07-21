# Enter your code here. Read input from STDIN. Print output to STDOUT
def discount(warpperleft,C1):
	freechoco=warpperleft/C1
	warpperleft=warpperleft%C1
	return freechoco,warpperleft
	
T = int(raw_input())
for i in range (0,T):
	A,B,C1 = [int(x) for x in raw_input().split(' ')]
	
	answer = A/B
	warpperleft=answer
	freechoco=0
	while warpperleft+freechoco>=C1:
		warpperleft+=freechoco
		freechoco,warpperleft=discount(warpperleft,C1)
		answer+=freechoco

	print answer
