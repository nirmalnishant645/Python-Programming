'''
An array/dictionary of lists is used. Size of the array/dictionary is equal to the number of vertices. Let the array be array[]. 
An entry array[i] represents the list of vertices adjacent to the ith vertex. This representation can also be used to represent a weighted graph. 
The weights of edges can be represented as lists of pairs.
'''

# Simple Directed Graph

class Graph:
    def __init__(self): # Initialise Graph
        self.graph = {}

    def insertEdge(self, val1, val2): # Insert Edge in the Graph
        if val1 in self.graph: # Check if vertex already exists
            self.graph[val1].append(val2) # Append the list directed by the vertex
        else:
            self.graph[val1] = [val2] # Add new vertex  if doesn't exist

    def  printGraph(self): # Print Graph
        for node in self.graph:
            for val in self.graph[node]:
                print(node, ' => ', val) # Loop through the dictionary and print each node and the node that it is pointing to
