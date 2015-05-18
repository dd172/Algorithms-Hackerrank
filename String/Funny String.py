#!usr/env/bin python

def solution(S):
	flag=1
	for i in range(len(S)):
		if abs(ord(S[i])-ord(S[i-1]))!=abs(ord(S[-i])-ord(S[-i-1])):
			flag=0
	if flag:
		print "Funny"
	else:
		print "Not Funny"

if __name__ == '__main__':
	T=int(raw_input())
	for _ in range(T):
		S=raw_input()
		solution(S)