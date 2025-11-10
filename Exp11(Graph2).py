class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0]*vertices for _ in range(vertices)]

    def addEdge(self, u, v, w):
        if u < self.v and v < self.v:
            self.graph[u][v] = w
            self.graph[v][u] = w

    def minDistance(self, dist, visited):
        min_val = 999999
        min_index = -1
        for i in range(self.v):
            if not visited[i] and dist[i] < min_val:
                min_val = dist[i]
                min_index = i
        return min_index

    def dijkstra(self, start):
        dist = [999999]*self.v
        visited = [False]*self.v
        dist[start] = 0

        for _ in range(self.v):
            u = self.minDistance(dist, visited)
            if u == -1:
                break
            visited[u] = True
            for v in range(self.v):
                if self.graph[u][v] > 0 and not visited[v]:
                    if dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]

        print("Minimum Time from Location", start, ":")
        for i in range(self.v):
            print("To", i, "=", dist[i])


v = int(input("Enter number of locations: "))
g = Graph(v)

while True:
    print("1. Add Route")
    print("2. Find Minimum Delivery Time (Dijkstra)")
    print("3. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        u = int(input("Enter starting location: "))
        v1 = int(input("Enter destination location: "))
        w = int(input("Enter time to reach (in mins): "))
        g.addEdge(u, v1, w)
    elif ch == 2:
        s = int(input("Enter starting location: "))
        g.dijkstra(s)
    elif ch == 3:
        break
    else:
        print("Invalid Choice")