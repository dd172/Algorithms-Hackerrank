
def solution(arr):
	if not len(arr)%2:
		count = 0
		arr1=arr[0:len(arr)/2]
		arr2=arr[len(arr)/2:len(arr)]
		arr0=set(arr)
		for element in arr0:
			count+=abs(arr1.count(element)-arr2.count(element))
		return count/2
	else:
		return -1

if __name__ == '__main__':
	T = int(raw_input())
	for _ in range(T):
		arr=raw_input()
		print solution(arr)
