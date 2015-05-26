# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python
def solution(L):
	best_sum=-2147483648
	current_sum=0
	for i in L:
		current_sum+=i
		if (current_sum > best_sum):
			best_sum = current_sum
		if (current_sum < 0):
			current_sum = 0
	
	add_all_positive=0
	for i in L:
		if i>0:
			add_all_positive+=i
		if add_all_positive==0:
			add_all_positive=max(L)

	print best_sum,add_all_positive
    
if __name__ == '__main__':
	T = int(raw_input())
	for _ in xrange(T):
		l = int(raw_input())
		
		L = map(int,raw_input().split())
		
		solution(L)