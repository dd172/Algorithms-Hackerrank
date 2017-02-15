import Queue
import fileinput

def solve(g,n,s):
    colors = {}
    distance = {}
    for i in range(1,n+1):
        colors[i] = 'white'
        distance[i] = -1

    colors[s] = 'gray'
    distance[s] = 0
    detect_queue = Queue.Queue()
    detect_queue.put(s)

    while not detect_queue.empty():


        gray_node = detect_queue.get()


        reach_list = []
        for i in range(1,n+1):
            if g[gray_node-1][i-1]:
                if colors[i] == 'white':
                    reach_list.append(i)


        for node in reach_list:
            reach_distance = []
            for i in range(1,n+1):
                if g[node-1][i-1]:
                    if colors[i] != 'white':
                        parent = i
                        reach_distance.append(distance[i]+g[node-1][i-1])

            distance[node] =min(reach_distance)


            colors[node] = 'gray'
            detect_queue.put(node)

        colors[gray_node] = 'black'
    for _ in range(1,n+1):
        if _ != s:
            print distance[_],
    print


if __name__ == '__main__':
    
    
    T= int(raw_input())
    
    for _ in range(T):
        N,E = (int(v) for v in raw_input().split())
        graph = [([0]*N) for i in range(N)]
        for _ in range(E):
            start,end,length = (int(v) for v in raw_input().split())
            if not graph[start-1][end-1] or graph[start-1][end-1]>length:
                graph[start-1][end-1],graph[end-1][start-1] = length,length

        S = int(raw_input())
        solve(graph,N,S)


