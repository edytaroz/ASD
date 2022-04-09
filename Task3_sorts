def partition1(tab,p,r):
    x = tab[r]
    i = p - 1
    for j in range(p,r):
        if tab[j] < x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[r],tab[i+1] = tab[i+1],tab[r]
    return i + 1
def quicksort1(tab,p,r):
    while p < r:
        q = partition1(tab,p,r)
        quicksort1(tab,p,q-1)
        p = q + 1

def SortTab(T, P):
    n = len(P)
    m = len(T)
    if m > 8:
        tab = [[] for _ in range(m//8)]
        for i in range(m):
            l = int(T[i])//8
            tab[l].append(T[i])
        for i in range(m//8):
            a = len(tab[i])
            if a > 1:
                quicksort1(tab[i],0, a-1)
        k = 0
        for i in range(m//8):
            a = len(tab[i])
            if a > 0:
                for j in range(a):
                    T[k] = tab[i][j]
                    k += 1
    else:
        tab = [[] for _ in range(m)]
        for i in range(m):
            l = int(T[i])
            tab[l].append(T[i])
        for i in range(m):
            a = len(tab[i])
            if a > 1:
                quicksort1(tab[i], 0, a - 1)
        k = 0
        for i in range(m):
            a = len(tab[i])
            if a > 0:
                for j in range(a):
                    T[k] = tab[i][j]
                    k += 1

    return T
