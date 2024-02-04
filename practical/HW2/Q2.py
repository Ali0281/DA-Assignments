import sys

sys.setrecursionlimit(2000000)


class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [set() for _ in range(self.V)]

    def is_bipartite(self):
        color = {}
        for n in range(self.V):
            if n not in color:
                neighbors, next_neighbors, curr_color = [n], [], True
                while neighbors:
                    p = neighbors.pop(0)
                    if p in color:
                        if color[p] != curr_color: return False
                    else:
                        color[p] = curr_color
                        for i in self.adj[p]:
                            next_neighbors.append(i)
                    if len(neighbors) == 0:
                        curr_color, neighbors, next_neighbors = not curr_color, next_neighbors, neighbors
        return True

    def NOCC(self):
        visits, c = [False] * self.V, 0
        for v in range(self.V):
            if not visits[v]:
                self.DFS(v, visits)
                c += 1
        return c

    def DFS(self, v, visits):
        visits[v] = True
        for i in self.adj[v]:
            if not visits[i]:
                self.DFS(i, visits)

    def add_edge(self, v, w):
        self.adj[w].add(v)
        self.adj[v].add(w)


students, enemies = map(int, input().split())

g = Graph(students)
for i in range(enemies):
    first, second = map(int, input().split())
    g.add_edge(first - 1, second - 1)

if not g.is_bipartite():
    print(0)
else:
    print(pow(2, g.NOCC() - 1, 10 ** 9 + 7))
