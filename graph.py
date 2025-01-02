class Graph:
    # Constructor
        # Adjacancy list
        def __init__(self, num_of_nodes, directed=True):
            self._num_of_nodes = num_of_nodes
            self._nodes = range(self._num_of_nodes)

            # Define the type of a graph
            self._directed = directed

            self._adj_list = {node: dict() for node in self._nodes}   

        # Adding edge
        def add_edge(self, node1, node2, weight=1):
            self._adj_list[node1].update({node2: weight})

            if not self._directed:
                self._adj_list[node2].update({node1: weight})

        # Removing edge
        def remove_edge(self, node1, node2, weight=1):
            self._adj_list[node1].pop(node2, weight)

        # Print adjacency list
        def print_adj_list(self):
            for key, value in self._adj_list.items():
                print(f"{key}: {value}")            
                
        # BFS
        def bfs(self, start, target):
            queue = [(start, [start])]
            while (queue):
                (node, path) = queue.pop(0)
                for neighbor in self._adj_list[node]:   
                    if neighbor not in path:
                        if (neighbor == target):
                            return path + [neighbor]
                        else:
                            queue.append((neighbor, path + [neighbor]))    

        # DFS
        def dfs(self, start_node):
            pass

        # Dijkstra
        def dijkstra(self, start_node):
            pass
    



graph = Graph(5)

graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(2, 5, 7)

print(graph.bfs(0, 4))

#graph.print_adj_list()