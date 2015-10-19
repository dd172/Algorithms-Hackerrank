

# def isPalindrome(s):
# 	flag=1
# 	for i in range(len(s)/2):
# 		if s[i]!=s[-1-i]:
# 			flag=0
# 			break
# 	if flag:
# 		return True
# 	else:
# 		return False

def isPalindrome2(s): #pythonic
	return s == s[::-1]


def isPalindrome3(s):
	p = 0
	for i in range(int(len(s)/2)):
		if s[i] == s[len(s) - 1 - i]:
			p+=1
	return p == int(len(s)/2)

def solution(s):
	index = -1
	lng = len(s)
	for i in range(lng/2):
		if s[i] !=s[lng-i-1]:
			if isPalindrome2(s[i+1:lng-i]):
				index = i
			else:
				index =lng - i - 1
			break
	return index
			
			

if __name__ == '__main__':
	T = int(raw_input())
	for _ in range(T):
		s = raw_input()
		print solution(s)