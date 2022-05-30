def partition(tab, p, r, l):
    x = tab[r][l]
    i = p - 1
    for j in range(p, r):
        if tab[j][l] < x:
            i += 1
            tab[j], tab[i] = tab[i], tab[j]
    tab[r], tab[i + 1] = tab[i + 1], tab[r]
    return i + 1


def quicksort(tab, p, r, l):
    while p < r:
        q = partition(tab, p, r, l)
        quicksort(tab, p, q - 1, l)
        p = q + 1

def bubble(tab,l):
    flag = True
    n = len(tab)
    while flag:
        fl = 0
        for i in range(1,n):
            if tab[i-1][l] > tab[i][l] and tab[i-1][l+1] == tab[i][l+1]:
                tab[i-1],tab[i] = tab[i],tab[i-1]
                fl = 1
        if fl == 0:
            flag = False

def new_building(B,i):
    l = 0
    r = i - 1
    mid = 0
    while l <= r:
        mid = l + (r-l)//2
        if B[i][1] > B[mid][2]:
            if B[i][1] > B[mid+1][2]:
                l = mid + 1
            else:
                return mid + 1
        else:
            r = mid - 1
    return -1


def zachodzenie(B,i,k):
    if B[i][1] == B[k][1] or B[i][2] == B[k][2] or B[i][1] == B[k][2] or B[i][2] == B[k][1]:
        return False
    if B[i][1] > B[k][1] and B[i][1] < B[k][2]:
        return False
    if B[i][2] > B[k][1] and B[i][2] < B[k][2]:
        return False
    return True


def try3(T,p):
    n = len(T)
    B = [[0 for _ in range(5)] for _ in range(n)]
    for i in range(n):
        B[i][0] = T[i][0] #wysokość
        B[i][1] = T[i][1] #początek
        B[i][2] = T[i][2] #koniec
        B[i][3] = T[i][3] #koszt
        B[i][4] = i
    quicksort(B,0,n-1,2)
    bubble(B,1)
    tab = [[0 for _ in range(p+1)] for _ in range(n)]
    tr = [[[0 for _ in range(n)] for _ in range(p+1)] for _ in range(n)]
    for b in range(B[0][3],p+1):
        studenci = B[0][0] * (B[0][2] - B[0][1])
        tab[0][b] = studenci
        tr[0][b][0] = 1
    for i in range(1, n):
        for b in range(B[i][3], p + 1):
            rem = B[i][0] * (B[i][2] - B[i][1])
            new = new_building(B,i)
            mk = 0
            remk = new
            if new != -1:
                for k in range(new+1):
                    if b - B[k][3] - B[i][3] >= 0 and zachodzenie(B,i,k):
                        if tab[k][b-B[i][3]] >= mk:
                            remk = k
                            mk = tab[k][b-B[i][3]]
            tab[i][b] = max(tab[i-1][b],rem+mk)
            if tab[i][b] == tab[i-1][b]:
                #tr[i][b] = tr[i-1][b]
                for j in range(n):
                    tr[i][b][j] = tr[i-1][b][j]
            else:
                #tr[i][b] = tr[remk][b-B[i][3]]
                for j in range(n):
                    tr[i][b][j] = tr[remk][b-B[i][3]][j]
                tr[i][b][i] = 1
    maks = 0
    rem = 0
    for i in range(n):
        if tab[i][p] > maks:
            rem = i
            maks = tab[i][p]
    q = []
    for i in range(n):
        if tr[rem][p][i] == 1:
            q.append(B[i][4])
    return q
