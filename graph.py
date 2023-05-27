import sys

def dijkstra(graph, start_node):
	num_nodes = len(graph)
	visited = [False] * num_nodes
	distances = [sys.maxsize] * num_nodes
	distances[start_node] = 0
	
	for _ in range(num_nodes):
		# Find the node with the minimum distance
		min_distance = sys.maxsize
		min_node = -1
		for node in range(num_nodes):
			if not visited[node] and distances[node] < min_distance:
				min_distance = distances[node]
				min_node = node
		
		if min_node == -1:
			break
		
		visited[min_node] = True
		
		# Update distances for the neighbors of the current node
		for neighbor in range(num_nodes):
			if (not visited[neighbor] and graph[min_node][neighbor] != 0
					and	distances[min_node] + graph[min_node][neighbor]
					< distances[neighbor]):
				distances[neighbor] = distances[min_node] + graph[min_node][neighbor]
	
	return distances

# Define the graph as a 2D list
graph = [[0, 7, 9, 0, 0, 14], [7, 0, 10, 15, 0, 0], [9, 10, 0, 11, 0, 2],
         [0, 15, 11, 0, 6, 0], [0, 0, 0, 6, 0, 9],[14, 0, 2, 0, 9, 0]]

start_node = 0  # Choose the starting node (0 to 5)

distances = dijkstra(graph, start_node)

# Print the shortest distances from the starting node to all other nodes
for node, distance in enumerate(distances):
	print(distance)
