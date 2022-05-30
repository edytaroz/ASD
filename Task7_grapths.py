#Algorytm przeprowadza DFS i gdy nie może iść dalej i nie odwiedził wszystkich
#miast cofa się i odznacza miasto, w którym był jako nieodwiedzone. Złożoność O(e^v)

def try5(G):
    def DFS(G):
        fl = True
        n = len(G)
        vis = [False for _ in range(n)]
        par = [0 for _ in range(n)]
        l = []
        def DFSVisit(G, u):
            nonlocal fl
            nonlocal l
            if fl:
                vis[u] = True
                if all(flag is True for flag in vis):
                    l = []
                    count = 0
                    while count != n:
                        count += 1
                        l.append(u)
                        u = par[u]
                    l.reverse()
                    rm = 0
                    rm2 = 0
                    if l[1] in G[l[0]][0]:
                        rm = 1
                    if l[len(l) - 2] in G[l[len(l) - 1]][0]:
                        rm2 = 1
                    if l[len(l) - 1] in G[l[0]][rm] and l[0] in G[l[len(l) - 1]][rm2]:
                        fl = False
                        return l
                k = par[u]
                rem = 0
                if k in G[u][0]:
                    rem = 1
                for i in range(len(G[u][rem])-1,-1,-1):
                    v = G[u][rem][i]
                    if not vis[v]:
                        par[v] = u
                        DFSVisit(G, v)
                        vis[v] = False

        for i in range(len(G[0][0])-1,-1,-1):
            if fl:
                par[G[0][0][i]] = 0
                DFSVisit(G, G[0][0][i])
                vis[G[0][0][i]] = False
        if not fl:
            return l
        return None
    return DFS(G)
