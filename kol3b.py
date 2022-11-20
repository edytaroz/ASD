from kol3btesty import runtests
from queue import PriorityQueue

def air1(G,A,s,t):
    n = len(G)
    vis = [False for _ in range(n)]
    d = [10**10 for _ in range(n)]
    par = [-1 for _ in range(n)]
    w = [[10**10 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            w[i][j[0]] = j[1]
    for i in range(n):
        for j in range(n):
            w[i][j] = min(A[i] + A[j],w[i][j])
    Q = PriorityQueue()
    d[s] = 0
    Q.put((0,s))
    while not Q.empty():
        u = Q.get()[1]
        for i in range(n):
            if w[u][i] != 10**10 and not vis[i]:
                if d[i] > d[u] + w[u][i]:
                    d[i] = d[u] + w[u][i]
                    par[i] = u
                    Q.put((d[i],i))
        vis[u] = True

    return d[t]

def better(G,A,s,t):
    n = len(G)
    vis = [False for _ in range(n)]
    d = [10 ** 10 for _ in range(n)]
    d2 = [10**10 for _ in range(n)]
    vis2 = [False for _ in range(n)]
    Q = PriorityQueue()
    d[s] = 0
    d2[t] = 0
    Q.put((0, s))
    while not Q.empty():
        u = Q.get()[1]
        for i in G[u]:
            if not vis[i[0]]:
                if d[i[0]] > d[u] + i[1]:
                    d[i[0]] = d[u] + i[1]
                    Q.put((d[i[0]], i[0]))
        vis[u] = True
    Q.put((0, t))
    while not Q.empty():
        u = Q.get()[1]
        for i in G[u]:
            if not vis2[i[0]]:
                if d2[i[0]] > d2[u] + i[1]:
                    d2[i[0]] = d2[u] + i[1]
                    Q.put((d2[i[0]], i[0]))
        vis2[u] = True
    sum = min(d[t],d2[s])
    for i in range(n):
        for j in range(n):
            if d[i] + d2[j] + A[i] + A[j] < sum:
                sum = d[i] + d2[j] + A[i] + A[j]
    return sum

def better2(G,A,s,t):
    n = len(G)
    G.append([])
    for i in range(n):
        G[i].append((n,A[i]))
        G[n].append((i,A[i]))
    n += 1
    vis = [False for _ in range(n)]
    d = [10 ** 10 for _ in range(n)]
    d[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))
    while not Q.empty():
        u = Q.get()[1]
        for i in G[u]:
            if not vis[i[0]]:
                if d[i[0]] > d[u] + i[1]:
                    d[i[0]] = d[u] + i[1]
                    Q.put((d[i[0]], i[0]))
        vis[u] = True
    return d[t]


def airports( G, A, s, t ):
    # tu prosze wpisac wlasna implementacje
    print(G)
    return better2(G,A,s,t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )
