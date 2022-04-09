def depth(L):
    def partition(tab, p, r):
        x = tab[r]
        i = p - 1
        for j in range(p,r):
            if tab[j] <= x:
                i += 1
                tab[i], tab[j] = tab[j], tab[i]
        tab[i + 1], tab[r] = tab[r], tab[i + 1]
        return i + 1

    n = len(L)
    tab2 = [[0 for _ in range(3)] for _ in range(n)]
    for i in range(n):
        tab2[i][0] = L[i][1] - L[i][0]
        tab2[i][1] = L[i][0]
        tab2[i][2] = L[i][1]
    S = [(-1, -1) for _ in range(n)]
    ptr = 0
    S[0] = (0, n - 1)
    while ptr >= 0:
        p, r = S[ptr]
        ptr -= 1
        q = partition(tab2, p, r)
        if p < q - 1:
            ptr += 1
            S[ptr] = (p, q - 1)
        if q + 1 < r:
            ptr += 1
            S[ptr] = (q + 1, r)

    dep = 0
    tab1 = [True for _ in range(n)]
    for i in range(n - 1, -1, -1):
        if n - dep > i:
            d = 0
            if tab1[i]:
                for j in range(i, -1, -1):
                    if i != j:
                        if tab2[i][1] <= tab2[j][1]:
                            if tab2[i][2] >= tab2[j][2]:
                                d += 1
                                tab1[j] = False
                if d > dep:
                    dep = d
    return dep
