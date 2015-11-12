if __name__ == '__main__':
	T = int(raw_input())
	arr = []
	for _ in range(T):
		arr.append(raw_input())
	
count = 0

arr0 = ''.join(set(arr[0]))

for char in arr0:
	flag=0
	for i in xrange(T-1):
		if char in arr[i+1]:
			flag=0
		else:
			flag=1
			break
	if not flag:
		count+=1

print count

