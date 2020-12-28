'''
The Implementation will be same as Directed Graph, but this time the connection will be done both ways.
If v1 => v2 then v2 => v1
Or v1 <=> v2
'''

# Simple Graph Implementation

class Graph:
    def __init__(self, number_of_nodes): # Initialise Graph Data Structure
        self.number_of_nodes = number_of_nodes + 1 # Number of nodes will have to be increased by one 
        self.graph = [[0 for x in range(number_of_nodes + 1)] for y in range(number_of_nodes + 1)]

    def withInBounds(self, v1, v2): # Function to check if the value is within matrix bounds
        return v1 >= 0 and v1 <= self.number_of_nodes and v2 >= 0 and v2 <=  self.number_of_nodes

    def insertEdge(self, v1, v2): # Function to inser edge in the Graph
        if self.withInBounds(v1, v2): # Check if values are within bounds
            self.graph[v1][v2] = 1 # Change the value of the node from 0 to 1
            self.graph[v2][v1] = 1 # Adding the two way relation between the vertices to make in undirected

    def printGraph(self): # Functipon to Print Graph
        for i in range(self.number_of_nodes):
            for j in range(len(self.graph[i])):
                if self.graph[i][j]:
                    print(i, '=>', j)

g = Graph(5)

g.insertEdge(1, 2)
g.insertEdge(2, 3)
g.insertEdge(4, 5)

g.printGraph()