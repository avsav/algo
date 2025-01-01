class Graph:
    # Constructor
        # Adjacancy list
        def __init__(self, num_of_nodes, directed=False):
            self._num_of_nodes = num_of_nodes
            self._nodes = range(self._num_of_nodes)

            # Define the type of a graph
            self._directed = directed

            self._adj_list = {node: set() for node in self._nodes}   

        # Adding edge
        def add_edge(self, node1, node2, weight=1):
            self._adj_list[node1].add((node2, weight))

            if not self._directed:
                self._adj_list[node2].add((node1, weight))

        # Removing edge
        def remove_edge(self, node1, node2):
            pass

        # Print adjacency list
        def print_adj_list(self):
            for key in self._adj_list.keys():
                print("node", key, ": ", self._adj_list[key])            
                
        # BFS
        def bfs(self):
            pass

        # DFS
        def dfs(self):
            pass

        # Dijkstra
        def dijkstra(self):
            pass
    



graph = Graph(5)

graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

graph.print_adj_list()