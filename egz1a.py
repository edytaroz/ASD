from egz1atesty import runtests
from queue import PriorityQueue


def frog(S):
    #S = S[0]
    n = len(S)
    maks = 0
    sum = 0
    st_snieg = 0
    Q = PriorityQueue()
    for i in range(n):
        Q.put(-S[i])
    for d in range(1,n+1):
        st_snieg += (d-1)
        a = abs(Q.get())
        sum += a
        sum -= st_snieg
        if sum > maks:
            maks = sum
        sum += st_snieg
        if st_snieg > maks:
            break
    return maks

def snow( S ):
    # tu prosze wpisac wlasna implementacje
    return frog(S)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
