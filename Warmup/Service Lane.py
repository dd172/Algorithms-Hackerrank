def solution(IN,OUT,lane):
    print min(lane[IN:OUT+1]) 

if __name__ == '__main__':
    
    N, T =map(int,raw_input().split())
    lane =raw_input().split() 

    for _ in range(T):
        IN, OUT =map(int,raw_input().split())
        solution(IN,OUT,lane)