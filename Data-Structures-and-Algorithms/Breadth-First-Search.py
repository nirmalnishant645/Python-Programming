'''
Graph traversal means visiting every vertex and edge exactly once in a well-defined order. 
While using certain graph algorithms, you must ensure that each vertex of the graph is visited exactly once. 
The order in which the vertices are visited are important and may depend upon the algorithm or question that 
you are solving.

During a traversal, it is important that you track which vertices have been visited. 
The most common way of tracking vertices is to mark them.
Breadth First Search (BFS)

There are many ways to traverse graphs. BFS is the most commonly used approach.
BFS is a traversing algorithm where you should start traversing from a selected node (source or starting node) 
and traverse the graph layerwise thus exploring the neighbour nodes (nodes which are directly connected to source node). 
You must then move towards the next-level neighbour nodes.

As the name BFS suggests, you are required to traverse the graph breadthwise as follows:
- First move horizontally and visit all the nodes of the current layer
- Move to the next layer

Time Complexity: O(V + E)
Space Complexity: O(V)
V is number of vertices (nodes), E is number of edges
'''

class Graph:
    def __init__(self):
        self.graph = {}

    def insertEdge(self, v1, v2):
        if v1 in self.graph:
            self.graph[v1].append(v2)
        else:
            self.graph[v1] = [v2]

    def BSF(self, start_node):
        visited, queue = {start_node}, [start_node]

        while queue:
            cur = queue.pop(0)
            print(cur, end = " ")

            if cur in self.graph:
               for node in self.graph[cur]:
                   if node not in visited:
                       queue.append(node)
                       visited.add(node)

g = Graph()

g.insertEdge(2, 1)
g.insertEdge(2, 5)
g.insertEdge(5, 6)
g.insertEdge(5, 8)
g.insertEdge(6, 9)

g.BSF(2)