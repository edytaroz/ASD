from collections import deque

#Algorytm przechodzi przez graf robiąc BFS. Znajduje w ten sposób najkrótszą
#ścieżkę z punktu s do punktu t, następnie sprawdza czy bez użycia kolejnych
#krawędzi najkrótsza droga jest większa od oryginalnej najkrótszej drogi. Jeśli
#tak to zwraca tą krawędź. Złożoność O(e*(v+e))
def len_sans(G,kr,s,t):
    Q = deque()
    n = len(G)
    vis = [False for _ in range(n)]
    d = [0 for _ in range(n)]
    Q.append(s)
    vis[s] = True
    while len(Q) > 0:
        u = Q.popleft()
        for v in G[u]:
            if not vis[v] and not (u == kr[1] and v == kr[0]):
                vis[v] = True
                d[v] = d[u] + 1
                Q.append(v)
    if d[t] == 0:
        return float('inf')
    return d[t]


def longer( G, s, t ):
    Q = deque()
    n = len(G)
    vis = [False for _ in range(n)]
    par = [0 for _ in range(n)]
    d = [0 for _ in range(n)]
    Q.append(s)
    vis[s] = True
    while len(Q) > 0:
        u = Q.popleft()
        for v in G[u]:
            if not vis[v]:
                vis[v] = True
                d[v] = d[u] + 1
                par[v] = u
                Q.append(v)
    tab = [t]
    v = t
    while v > 0:
        tab.append(par[v])
        v = par[v]
    rem = d[t]
    para = None
    flag = True
    for i in range(1, len(tab)):
        if flag:
            kr = (tab[i - 1], tab[i])
            if rem < len_sans(G, kr, s, t):
                para = (tab[i], tab[i - 1])
                flag = False
    return para
