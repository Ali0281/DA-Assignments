def breadth_search(graph, s, t, parent):
    visits, que = [False] * len(graph), [s]
    visits[s] = True
    while que:
        u = que.pop(0)
        ind = 0
        for val in graph[u]:
            if visits[ind] is False:
                if val > 0:
                    que.append(ind)
                    visits[ind], parent[ind] = True, u
                    if ind == t:
                        return True
            ind += 1
    return False


def ford(graph, source, sink):
    parent, M_flow = [-1] * len(graph), 0
    while breadth_search(graph, source, sink, parent) is True:
        P_flow = float("Inf")
        s = sink
        while s != source:
            P_flow = P_flow if P_flow < graph[parent[s]][s] else graph[parent[s]][s]
            s = parent[s]
        M_flow += P_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v], graph[v][u] = graph[u][v] - P_flow, graph[v][u] + P_flow
            v = parent[v]
    return M_flow


CE, CS, link = list(map(int, input().split()))
v = CE + CS + 2  # add s and t
graph = [[0] * v for i in range(v)]
pair = [[0] * CS for i in range(CE)]

start, end = None, None
for i in range(link):
    start, end = list(map(int, input().split()))
    pair[start - 1][end - 1] = 1

WCE = list(map(int, input().split()))
WCS = list(map(int, input().split()))

for i in range(CE): graph[0][i + 1] = WCE[i]
for i in range(CS): graph[i + CE + 1][CE + CS + 1] = WCS[i]

for i in range(CE):
    for j in range(CS):
        if pair[i][j] == 0: graph[1 + i][1 + CE + j] = float("Inf")

print(sum(WCS) + sum(WCE) - ford(graph, 0, v - 1))
