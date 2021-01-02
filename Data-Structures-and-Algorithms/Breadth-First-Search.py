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