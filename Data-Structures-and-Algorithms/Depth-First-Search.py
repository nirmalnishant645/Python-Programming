'''
The DFS algorithm is a recursive algorithm that uses the idea of backtracking. It involves exhaustive searches of all 
the nodes by going ahead, if possible, else by backtracking.
Here, the word backtrack means that when you are moving forward and there are no more nodes along the current path, 
you move backwards on the same path to find nodes to traverse. All the nodes will be visited on the current path 
till all the unvisited nodes have been traversed after which the next path will be selected.
This recursive nature of DFS can be implemented using stacks. The basic idea is as follows:
Pick a starting node and push all its adjacent nodes into a stack.
Pop a node from stack to select the next node to visit and push all its adjacent nodes into a stack.
Repeat this process until the stack is empty. However, ensure that the nodes that are visited are marked. 
This will prevent you from visiting the same node more than once. If you do not mark the nodes that are visited 
and you visit the same node more than once, you may end up in an infinite loop.

Time Complexity: O(V + E)
Space Complexity: O(V)
V is number of vertices (nodes), E is number of edges
'''

# Iterative DFS using Stack

class Graph:
    def __init__(self):
        self.graph = {}

    def insertEdge(self, v1, v2):
        if v1 in self.graph:
            self.graph[v1].append(v2)
        else:
            self.graph[v1] = [v2]

    def DFS(self, start_node):
        visited, stack = set(), [start_node]

        while stack:
            cur = stack[-1]
            stack.pop()

            if cur not in visited:
                print(cur, end = " ")
                visited.add(cur)
            
            if cur in self.graph:
                for node in self.graph[cur]:
                    if node not in visited:
                        stack.append(node)

# Recursive DFS

class Graph:
    def __init__(self):
        self.graph = {}

    def insertEdge(self, v1, v2):
        if v1 in self.graph:
            self.graph[v1].append(v2)
        else:
            self.graph[v1] = [v2]

    def DFS(self, start, visited = None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end = " ")
        if start in self.graph:
            for node in self.graph[start]:
                if node not in visited:
                    self.DFS(node, visited)
        return visited

g = Graph()

g.insertEdge(2, 1)
g.insertEdge(2, 5)
g.insertEdge(5, 6)
g.insertEdge(5, 8)
g.insertEdge(6, 9)

g.DFS(2)