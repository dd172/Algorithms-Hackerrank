def solution(arr):
    t=0
    l=len(arr)
    for x in range(l/2):
        t+=abs(ord(arr[x])-ord(arr[-x-1]))
    return t
 
 
if __name__ == '__main__':
    T=int(raw_input())
    for _ in range(T):
        arr = raw_input().strip()
        print solution(arr)