# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
stone=[]
for _ in xrange(T):
	stone.append(raw_input())
	stone[0]=str(set(stone[0]))
for letter in stone[0]:
	for i in xrange(1,len(stone)):
		if stone[i].find(letter)==0:
			stone[0].strip(letter)

print stone[0]
