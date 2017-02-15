import Queue

class graph(object):
	"""docstring for graph"""
	def __init__(self,graph_dict):
		self.graph_dict = graph_dict  
		self.nodes = graph_dict.keys()

	def init(self,graph_dict):
		self.nodes = graph_dict.keys()

	def BFS(self,s):

		detect_queue = Queue.Queue()

		colors = {}
		distance = {}
		parents = {}

		for node in self.nodes:
			colors[node] = 'white'
			distance[node] = -1
			parents[node] = None
		colors[s] = 'gray'
		distance[s] = 0
		detect_queue.put(s)

		while not detect_queue.empty():
			gray_node = detect_queue.get()
			reach_list = self.graph_dict[gray_node]
			
			for node in reach_list:
				if colors[node] == 'white':
					colors[node] = 'gray'
					distance[node] = distance[gray_node] + 6
					parents[node] = gray_node
					detect_queue.put(node)
			colors[gray_node] = 'black'

		for i in distance:
			if distance[i]:
				print distance[i],
		print
		
def main():
	N,M = (int(v) for v in raw_input().split())
	g=graph({})
	for i in range(1,N+1):
		g.graph_dict[i] = []
	for j in range(M):
		start,end =(int(v) for v in raw_input().split())
		g.graph_dict[start].append(end)
		g.graph_dict[end].append(start)

	g.nodes = g.graph_dict.keys()
	
	
	S = input()

	g.BFS(S)



if __name__ == '__main__':
	T = int(input())
	for _ in range(T):
		main()