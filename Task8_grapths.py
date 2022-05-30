from math import sqrt
from math import ceil

#Algorytm tworzy tablice krawędzi i ich wag, a następnie ją sortuje niemalejąco
#względem wag-długości krawędzi. Następnie idzie od początku i tworzy MST według
#Kruskalla. Jeśli różnica pomiędzy największą a najmniejszą krawędzię jest mniejsza
#niż dotychczasowa,to ją zapamiętuje.


class Node:
    def __init__(self,value):
        self.parent = self
        self.value = value
        self.rank = 0

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
       y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def try3(G):
    n = len(G)
    nods = []
    for i in range(n):
        nods.append(Node(i))
    range1 = n * (n - 1) // 2
    tab = []
    for i in range(n):
        for j in range(i + 1, n):
            a = (G[i][0] - G[j][0]) * (G[i][0] - G[j][0])
            b = (G[i][1] - G[j][1]) * (G[i][1] - G[j][1])
            rue = ceil(sqrt(a + b))
            p = [nods[i], nods[j], rue]
            tab.append(p)
    tab.sort(key=lambda x: x[2])
    j = 0
    diff = 10**10
    while j < range1 - n:
        t = []
        i = j
        mins = tab[j][2]
        maks = 0
        while len(t) != n - 1 and i < range1 and tab[i][2] - mins < diff:
            v = tab[i][0]
            u = tab[i][1]
            if find(v) != find(u):
                t.append([v,u])
                union(v, u)
                maks = tab[i][2]
            i += 1
        j += 1
        if maks - mins < diff and len(t) == n - 1:
            diff = maks - mins
        for k in range(n):
            a = nods[k]
            a.parent = a
            a.rank = 0
            nods[k] = a
    return diff
