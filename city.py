class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.matrix = [[0]*vertices for _ in range(vertices)]
        self.adj_list = [[] for _ in range(vertices)]

    def addEdge(self, u, v):
        if u < self.v and v < self.v:
            self.matrix[u][v] = 1
            self.matrix[v][u] = 1
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

    def dfsUtil(self, node, visited):
        print(node, end=" ")
        visited[node] = True
        for i in range(self.v):
            if self.matrix[node][i] == 1 and not visited[i]:
                self.dfsUtil(i, visited)

    def DFS(self, start):
        visited = [False]*self.v
        print("DFS Traversal (Adjacency Matrix):")
        self.dfsUtil(start, visited)

    def BFS(self, start):
        visited = [False]*self.v
        queue = []
        queue.append(start)
        visited[start] = True
        print("BFS Traversal (Adjacency List):")
        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)


v = int(input("Enter number of vertices: "))
g = Graph(v)

while True:
    print("\n1. Add Edge")
    print("2. Display DFS Traversal")
    print("3. Display BFS Traversal")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        u = int(input("Enter first vertex: "))
        v1 = int(input("Enter second vertex: "))
        g.addEdge(u, v1)
    elif ch == 2:
        s = int(input("Enter starting vertex for DFS: "))
        g.DFS(s)
        print()
    elif ch == 3:
        s = int(input("Enter starting vertex for BFS: "))
        g.BFS(s)
        print()
    elif ch == 4:
        break
    else:
        print("Invalid Choice")
