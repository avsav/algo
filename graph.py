class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self._num_of_nodes = num_of_nodes
        self._nodes = range(self._num_of_nodes)

        # Define the type of a graph
        self._directed = directed
        # Adjacancy list
        self._adj_list = {node: dict() for node in self._nodes}   

    # Adding edge
    def add_edge(self, node1, node2, weight=1):
        self._adj_list[node1].update({node2: weight})

        if not self._directed:
            self._adj_list[node2].update({node1: weight})

    # Removing edge
    def remove_edge(self, node1, node2, weight=1):
        self._adj_list[node1].pop(node2, weight)

    # Removing node
    def remove_node(self, node):
        pass

    # Print adjacency list
    def print_adj_list(self):
        for key, value in self._adj_list.items():
            print(f"{key}: {value}")            
            
    # BFS
    def bfs(self, start, target):
        dist = 0
        queue = [(start, [start], dist)]

        while (queue):
            (node, path, dist) = queue.pop(0)
            for neighbor, weight in self._adj_list[node].items():   
                if neighbor not in path:
                    if (neighbor == target):
                        return path + [neighbor], dist + weight
                    else:
                        queue.append((neighbor, path + [neighbor], dist + weight))    

    # DFS
    def dfs(self, start, target):
        dist = 0
        stack = [(start, [start], dist)]

        while (stack):
            (node, path, dist) = stack.pop()
            for neighbor, weight in self._adj_list[node].items():   
                if neighbor not in path:
                    if (neighbor == target):
                        return path + [neighbor], dist + weight
                    else:
                        stack.append((neighbor, path + [neighbor], dist + weight))    

    # Dijkstra
    def dijkstra(self, start, target):
        INF = 10**10

        # All nodes initially unvisited
        unvisited = self._adj_list.copy()

        dist_from_start = {
            node: (13 if node == start else INF) for node in self._nodes
        }

        while (unvisited):
            current = min(
                unvisited, key=lambda node: dist_from_start[node]
            )    
            #unvisited.pop()


        


    



graph1 = Graph(9)
graph1.add_edge(0, 1, 5)
graph1.add_edge(0, 2, 3)
graph1.add_edge(1, 3, 1)
graph1.add_edge(1, 4, 15)
graph1.add_edge(1, 7, 6)
graph1.add_edge(2, 5, 7)
graph1.add_edge(3, 6, 4)
graph1.add_edge(3, 7, 8)
graph1.add_edge(2, 8, 9)
graph1.add_edge(5, 7, 2)

graph2 = Graph(5)
graph2.add_edge(0, 1, 5)
graph2.add_edge(0, 2, 3)
graph2.add_edge(1, 3, 1)
graph2.add_edge(1, 4, 15)
graph2.add_edge(3, 4, 11)
graph2.add_edge(4, 2, 7)

# For Dijkstra
graph3 = Graph(5)
graph3.add_edge(0, 1, 4)
graph3.add_edge(0, 2, 2)
graph3.add_edge(1, 2, 3)
graph3.add_edge(1, 3, 2)
graph3.add_edge(1, 4, 3)
graph3.add_edge(2, 1, 1)
graph3.add_edge(2, 3, 4)
graph3.add_edge(2, 4, 5)
graph3.add_edge(4, 3, 1)


#print(graph1.bfs(0, 7))
#print(graph1.dfs(0, 7))

#graph1.print_adj_list()

graph3.dijkstra(0, 3)